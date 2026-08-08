#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
لینک‌ساز VLESS+Reality — لینک‌های درست هر ۴ سرور با TCP proxy.

استفاده:
    python3 xui-link-maker.py <UUID>
    یا
    export XUI_UUID="..." && python3 xui-link-maker.py

نکته: لینک‌هایی که خود پنل 3x-ui می‌سازد کار نمی‌کنند چون:
  - دامنه‌های .up.railway.app TLS خود Railway را تحمیل می‌کنند (x509 mismatch)
  - پورت اینباند (443) با پورت TCP proxy فرق دارد
  این اسکریپت آدرس TCP proxy + پورت درست را استفاده می‌کند.
"""

import os
import sys

SNI = "is1-ssl.mzstatic.com"
FP = "ios"
TYPE = "tcp"

# name → (tcp proxy domain, port, publicKey, shortId)
SERVERS = {
    "NL":    ("reseau.proxy.rlwy.net", 25816, "BRmgS2SxcaLw-cUXm6buHTCdE6wP1nWHU_qPkmKuzGA", "6fd63174"),
    "SG":    ("turntable.proxy.rlwy.net", 16139, "0Tyvs8SuDmRyHym-dj-fxxOtJ8xVIsFdh0Dby6zEnUE", "96726748"),
    "US-VA": ("autorack.proxy.rlwy.net", 58343, "j5JvDvTAvjar_b_M2RNmeGlIoCss9zNgtbqN5GspAnA", "e7be5aa5"),
    "US-CA": ("reseau.proxy.rlwy.net", 54117, "ewVcmLWfMq3xIyOrmDApg7FstfHhQuHUaB_wDHPbzHA", "73548b14"),
}


def main():
    uuid_val = os.environ.get("XUI_UUID", "")
    if len(sys.argv) > 1:
        uuid_val = sys.argv[1]
    if not uuid_val:
        print("❌ UUID را بده:  python3 xui-link-maker.py <UUID>")
        return 1

    print(f"🔗 لینک‌های اتصال (UUID: {uuid_val})\n" + "=" * 55)
    for name, (host, port, pbk, sid) in SERVERS.items():
        link = (f"vless://{uuid_val}@{host}:{port}"
                f"?encryption=none&security=reality&sni={SNI}&fp={FP}"
                f"&pbk={pbk}&sid={sid}&type={TYPE}&headerType=none"
                f"#{name}")
        print(f"\n{name} ({host}:{port}):")
        print(f"  {link}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
