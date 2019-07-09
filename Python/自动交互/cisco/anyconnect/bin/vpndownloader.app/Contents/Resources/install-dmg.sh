#!/bin/sh
# Script for installing DMG packges for AnyConnect, intended for invocation by Downloader

BASH_BASE_SIZE=0x00000619
CISCO_AC_TIMESTAMP=0x000000005aad90b3
CISCO_AC_OBJNAME=install-dmg.sh                                                  
# BASH_BASE_SIZE=0x00000000 is required for signing
# CISCO_AC_TIMESTAMP is also required for signing
# comment is after BASH_BASE_SIZE or else sign tool will find the comment

readonly RET_PARAM_ERROR=1
readonly RET_DMG_ERROR=2
readonly RET_PKG_ERROR=3

LOG_FACILITY="install.notice"
LOG_TOPIC="install-dmg.sh"

log()
{
    logger -p "$LOG_FACILITY" -t "$LOG_TOPIC" $1
}

if [ "x${1}" != "x" ]; then
    DMG=$1
    PKG=$(basename "${1%.*}").pkg
else
    echo "$0 <path to AnyConnect disk image> <AnyConnect installer name>" | log
    exit ${RET_PARAM_ERROR}
fi

echo "Installing ${PKG} from ${DMG}" | log

# Mount the DMG and take note of mount path
echo "hdiutil attach ${DMG} -nobrowse -noverify" | log
HDIUTILOUT=$(hdiutil attach ${DMG} -nobrowse -noverify) || exit ${RET_DMG_ERROR} 

MOUNTPATH=$(echo "${HDIUTILOUT}" | egrep -o "(/Volumes/.*)")

# this will be invoked when we trap exit
unmount_dmg()
{
    # Unmount the DMG
    echo "hdiutil eject ${MOUNTPATH} -force" | log
    hdiutil eject "${MOUNTPATH}" -force || exit ${RET_DMG_ERROR}
}
trap unmount_dmg EXIT

# Execute the installer
echo "installer -pkg \"${MOUNTPATH}/${PKG}\" -target \"/\" -verbose" | log
installer -pkg "${MOUNTPATH}/${PKG}" -target "/" -verbose || exit ${RET_PKG_ERROR}

# Finished!
echo "Finished installing ${PKG}" | log

exit 0
  +S!cV!j!dqeayIVDMPT!A!kfkjvddSBJJJ!V!eznRGBF �0��0�ޠ;_5�?@a��AJ��0	*�H�� 010	UUS10U
Symantec Corporation10USymantec Trust Network100.U'Symantec Class 3 SHA256 Code Signing CA0160429000000Z180729235959Z0��10	UUS10U
California10USan Jose10U
Cisco Systems, Inc.10UEndpoint Security10UCisco Systems, Inc.0�"0	*�H�� � 0�
� �l-�n��7�EK\�A[��*O���������/l� #H8���k���1F�q��}ۀ���8����ar��$�������{�t+��Eq�@m؛q��Z��'8��p��P� 7�ڢT��bg׿$��w�x���:��	~A�  ��g��HxVK�I��	�z�C!�\u�w�d8��GH�F���?$\G˭���(�ތ����Ig�W-�kJv�����sA�Z��!)�t�M��\/��er449��^�t; ��]0�Y0	U0 0U��0+U$0"0 ���http://sv.symcb.com/sv.crl0aU Z0X0Vg�0L0#+https://d.symcb.com/cps0%+0https://d.symcb.com/rpa0U%0
+0W+K0I0+0�http://sv.symcd.com0&+0�http://sv.symcb.com/sv.crt0U#0��;S�y3��}��.+�ʷ�rf0Uv�_$Yؑ�j'
�ިی>0	*�H�� � 3��e��[!�}���	��j�G�-�D�::FZ�i�`f�]����_HD�G
9�wQ�����+^:&[�b�ɓ�,��V^|�6	o��C����w}�_u
����4�� ��E�����KT(m�}�e��7&٢}��ٌ;�����\*��ꎅ��F#�J1����+ 8?9fR?��˸�q�_/]\�m0oA�̭��m�ۥ�����Λ�]�����u�*��mJ��|�՞x��T[�~�A&=f��e ]0�Y0�A�=x��vI`�a}��ʆ*0	*�H�� 0��10	UUS10U
VeriSign, Inc.10UVeriSign Trust Network1:08U1(c) 2006 VeriSign, Inc. - For authorized use only1E0CU<VeriSign Class 3 Public Primary Certification Authority - G50131210000000Z231209235959Z010	UUS10U
Symantec Corporation10USymantec Trust Network100.U'Symantec Class 3 SHA256 Code Signing CA0�"0	*�H�� � 0�
� �� �,����h�Q`q��G��XM#bj��ZQ��wh��6�/!Pڞ��_'N�	p���\N�����ΑrT.Σ�D�R?A<�J���9�S�!�������Xj��=6�ŗ$��{�1-=nܵ�B�Ka�_p�}ۋ�a�x�h�x���UGSٳ2֡F@ŗ���S��[�5W��ba 
�0w$Mb���{h�1�e���Ս�5܌+ojr\`����^�VR H����}�/��8���F�����Z8ݛ� ���0�0/+#0!0+0�http://s2.symcb.com0U�0� 0lU e0c0a`�H��E0R0&+http://www.symauth.com/cps0(+0http://www.symauth.com/rpa00U)0'0%�#�!�http://s1.symcb.com/pca3-g5.crl0U%0++0U�0)U"0 �010USymantecPKI-1-5670U�;S�y3��}��.+�ʷ�rf0U#0��e�����0	�C9��3130	*�H�� � �i�7�����~aS���^�ux#���U9�q��eZ��0�DZa�po�!�.s�I�ѓ�]��^���?t��8���ϻ5/3X��V��M;��y��(��G��>�٦�V�?��.)�|����=꺓�P")L��:_֤%��k/��L'{�"�`?���ML��rgw�'�Ǻ5�I���(�J����D�6+��P�]��'KT�+�^��t
�É"�w��C��L�?����d��! o ��F+�k�j���A�
�^��������.o��n8G�1�z���b�(1݁����䊼�I
7�ڋ�\�J����Ӏ0�J�!OV��/���{Xѣ �n��.�����*���cox�Q�(��(Q��0{/�<�'V�p�8�;I�а�
2��k���߽_>�T��!�/ :p��!;��u��x�V!���g����y�xR�9�m�b�=Α���1[(=�/���k
��^��៕����(�  ��F+�k�j���A�
�^��������.o��n8G�1�z���b�(1݁����䊼�I
7�ڋ�\�J����Ӏ0�J�!OV��/���{Xѣ �n��.�����*���cox�Q�(��(Q��0{/�<�'V�p�8�;I�а�
2��k���߽_>�T��!�/ :p��!;��u��x�V!���g����y�xR�9�m�b�=Α���1[(=�/���k
��^��៕����(�  �Id�jlXc�c_Fج�5s*��d���˸ZǮ_:�je�6p+�*3�����Y'y\0n�6�_>:U=�k}2T��Ja�l}�4����G�ڜ횞׈%ޜ� u�n����$����%P�34���Xԡ[���H
>o����. ̒P��N׆ޓ�hќ���< x��*���? W�t�_=���i��x�NF¿i��wI�z��o6
{����f��p92+�B���F��-L�8%y���:�a�x