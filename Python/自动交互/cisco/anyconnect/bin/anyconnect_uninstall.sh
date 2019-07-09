#!/bin/sh

ANYCONNECT_APPLICATIONNAME="Cisco AnyConnect Secure Mobility Client"

ANYCONNECT_BINDIR="/opt/cisco/anyconnect/bin"
POSTURE_BINDIR="/opt/cisco/hostscan/bin"

VPN_UNINST=${ANYCONNECT_BINDIR}/vpn_uninstall.sh
WEBSECURITY_UNINST=${ANYCONNECT_BINDIR}/websecurity_uninstall.sh
FIREAMP_UNINST=${ANYCONNECT_BINDIR}/amp_uninstall.sh
POSTURE_UNINST=${POSTURE_BINDIR}/posture_uninstall.sh
ISEPOSTURE_UNINST=${ANYCONNECT_BINDIR}/iseposture_uninstall.sh
ISECOMPLIANCE_UNINST=${ANYCONNECT_BINDIR}/isecompliance_uninstall.sh
NVM_UNINST=${ANYCONNECT_BINDIR}/nvm_uninstall.sh
OPENDNS_UNINST=${ANYCONNECT_BINDIR}/umbrella_uninstall.sh

# Gracefully quit the AnyConnect App prior to running uninstall script(s)
echo "Exiting ${ANYCONNECT_APPLICATIONNAME}"
osascript -e "quit app \"${ANYCONNECT_APPLICATIONNAME}\"" > /dev/null 2>&1

if [ -x "${ISEPOSTURE_UNINST}" ]; then
  ${ISEPOSTURE_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect ISE Posture Module."
  fi
fi

if [ -x "${ISECOMPLIANCE_UNINST}" ]; then
  ${ISECOMPLIANCE_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect ISE Compliance Module."
  fi
fi

if [ -x "${POSTURE_UNINST}" ]; then
  ${POSTURE_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect Posture Module."
  fi
fi

if [ -x "${WEBSECURITY_UNINST}" ]; then
  ${WEBSECURITY_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect Web Security Module."
  fi
fi

if [ -x "${OPENDNS_UNINST}" ]; then
  ${OPENDNS_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect Roaming Security Module."
  fi
fi

if [ -x "${FIREAMP_UNINST}" ]; then
  ${FIREAMP_UNINST}
  if [ $? -ne 0 ]; then
  echo "Error uninstalling AMP Enabler Module."
  fi
fi

if [ -x "${NVM_UNINST}" ]; then
  ${NVM_UNINST}
  if [ $? -ne 0 ]; then
  echo "Error uninstalling Network Visibility Module."
  fi
fi

if [ -x "${VPN_UNINST}" ]; then
  ${VPN_UNINST}
  if [ $? -ne 0 ]; then
    echo "Error uninstalling AnyConnect Secure Mobility Client."
  fi
fi

exit 0
