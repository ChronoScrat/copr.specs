# Inspired by: https://github.com/ublue-os/packages/blob/main/Justfile

export builder_registry := env("BUILDER_REGISTRY","ghcr.io/chronoscrat")
export builder_image := env("BUILDER_IMAGE","fedora-devel")
export builder_tag := env("BUILDER_TAG","latest")


# Build RPM: This recipe will build the RPM. It's primarely meant to be run
# inside a devcontainer.

build $SPEC_FILE *MOCK_ARGS:
    #!/usr/bin/bash
    set -x

    OUTDIR="${OUTDIR:-/tmp/rpmbuild}"
    SPEC_PATH=$(realpath $SPEC_FILE)
    SPEC_NAME=$(basename $SPEC_PATH)
    SPEC_DIR=$(dirname $SPEC_PATH)

    if [ -d ${OUTDIR} ]; then
        rm -fr ${OUTDIR}
    fi

    mkdir ${OUTDIR}

    rpkg spec --spec ${SPEC_PATH} --outdir ${OUTDIR}
    cp ${SPEC_DIR}/*.patch ${OUTDIR}
    rpmlint ${OUTDIR}/${SPEC_NAME}
    spectool -ga ${OUTDIR}/${SPEC_NAME} --directory ${OUTDIR}
    rpkg --path ${SPEC_DIR} srpm --outdir ${OUTDIR}

    mock --spec ${OUTDIR}/${SPEC_NAME} --sources ${OUTDIR} --resultdir ${OUTDIR} {{ MOCK_ARGS }}

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
