ERRVAL=0
/opt/cisco/anyconnect/bin/vpndownloader.app/Contents/MacOS/vpndownloader "$*" || ERRVAL=$?
exit ${ERRVAL}
