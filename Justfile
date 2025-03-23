# Inspired by: https://github.com/ublue-os/packages/blob/main/Justfile

build $SPEC_FILE $MOCK_ARGS:
    #!/usr/bin/bash
    set -x

    OUTDIR="${OUTDIR:-/tmp/rpmbuild}"
    SPEC_PATH=$(realpath $SPEC_FILE)
    SPEC_NAME=$(basename $SPEC_PATH)

    if [ -d ${OUTDIR} ]; then
        rm -fr ${OUTDIR}
    fi

    mkdir ${OUTDIR}

    rpkg spec --spec ${SPEC_PATH} --outdir ${OUTDIR}
    rpmlint ${OUTDIR}/${SPEC_NAME}
    spectool -ga ${OUTDIR}/${SPEC_NAME} --directory ${OUTDIR}
    rpkg --path ${OUTDIR} srpm --outdir ${OUTDIR}

    mock --spec ${OUTDIR}/${SPEC_NAME} --sources ${OUTDIR} --resultdir ${OUTDIR} $MOCK_ARGS