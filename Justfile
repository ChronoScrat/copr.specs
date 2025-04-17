# Inspired by: https://github.com/ublue-os/packages/blob/main/Justfile

export builder_registry := env("BUILDER_REGISTRY","ghcr.io/chronoscrat")
export builder_image := env("BUILDER_IMAGE","fedora-devel")
export builder_tag := env("BUILDER_TAG","latest")


# Build RPM: This recipe will build the RPM. It's primarely meant to be run
# inside a devcontainer.

build $SPEC_FILE *MOCK_ARGS:
    #!/usr/bin/bash
    set +x

    OUTDIR="${OUTDIR:-/tmp/rpmbuild}"
    SPEC_PATH=$(realpath $SPEC_FILE)
    SPEC_NAME=$(basename $SPEC_PATH)
    SPEC_DIR=$(dirname $SPEC_PATH)

    echo -e "\033[1;33m 🚧 Setting build directory at \033[1;37m ${OUTDIR} \033[0m"

    if [ -d ${OUTDIR} ]; then
        rm -fr ${OUTDIR}
    fi

    mkdir ${OUTDIR}

    echo -e "\033[1;35m 🔍 Creating final SPEC file from template at\033[1;37m ${SPEC_FILE} \033[0m"
    rpkg spec --spec ${SPEC_PATH} --outdir ${OUTDIR}

    echo -e "\033[1;33m 📄 Copying all patches to\033[1;37m ${OUTDIR} \033[0m"
    cp ${SPEC_DIR}/*.patch ${OUTDIR}

    echo -e "\033[1;33m 🔍 Linting final SPEC file \033[0m"
    rpmlint ${OUTDIR}/${SPEC_NAME}

    echo -e "\033[1;35m ⬇️  Downloading all sources and remote patches to\033[1;37m ${OUTDIR} \033[0m"
    spectool -ga ${OUTDIR}/${SPEC_NAME} --directory ${OUTDIR}

    echo -e "\033[1;35m 🔍 Creating source RPM at\033[1;37m ${OUTDIR} \033[0m"
    rpkg --path ${SPEC_DIR} srpm --outdir ${OUTDIR}

    echo -e "\033[1;36m 📦 Building package \033[0m"
    mock --spec ${OUTDIR}/${SPEC_NAME} --sources ${OUTDIR} --resultdir ${OUTDIR} {{ MOCK_ARGS }}

    echo -e "\033[1;32m ✅ Build Complete! All files are available at\033[1;37m ${OUTDIR} \033[0m"

# CI: This recipe will be run inside Github actions. It is the same as the build rpm recipe,
# but run inside a container.

# To simplify my life, this recipe will be run with network access by default.

ci $SPEC_FILE *MOCK_ARGS:
    #!/usr/bin/bash
    set -x

    SPECS_DIR="${SPECS_DIR:-.}"
    IMAGE="${builder_registry}/${builder_image}:${builder_tag}"

    podman=$(which podman)

    ${podman} run -it --rm \
        --privileged \
        --pull "newer" \
        -v ${SPECS_DIR}:/tmp/workspace:Z \
        -w /tmp/workspace \
        ${IMAGE} \
        just build ${SPEC_FILE} {{ MOCK_ARGS }}
