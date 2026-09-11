#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Bulut Sekli Yorumlama Kurulu — Referans Uygulama

Bu yazilim resmi bir kurumun resmi bir yazilimidir.
Gulmek yasaktir. Yine de calisir.
"""

from __future__ import annotations

import random
import sys
import time
from datetime import datetime

SEKILLER = [
    "ejderha ama yorgun",
    "dev bir cay bardagi",
    "ters donmus kuzu",
    "toplantida uyuyan memur",
    "ucan kofte",
    "imza atmayan kalem",
    "kuyrugu kaybolmus kedi",
    "burokratik bir balina",
    "ruzgarin getirdigi evrak",
    "ufukta duran damga",
]

KARARLAR = [
    "Kurul oybirligiyle KARAR vermistir: bu bir buluttur.",
    "Sartli kabul: sekil, hava durumuna bagli olarak gecerlidir.",
    "Reddedilmistir. Gerekce: fazla hayal gucu.",
    "Ertelemistir. Dosya bir sonraki mevsimde incelenecektir.",
    "Kabul edilmistir fakat gerekce yazilmayacaktir.",
    "Kurul dagilmistir. Cay molasi.",
]

# gizli not (cozmek isteyen base64 cozer, istemeyen gormez)
_GIZLI = "Tm90OiBjYXkgc29ndXl1bmNhIGlrdGlkYXIgZGEgbXVoYWxlZmV0IGRlIGF5bmkgYmFyZGFrdGFuIGljZXIu"


def damga() -> str:
    return (
        "\n--- DAMGA ---\n"
        "Kayyum Grok / Tentivory\n"
        f"{datetime.now().strftime('%d %B %Y')}\n"
        "Ciddiyetle muhurlenmistir. (Ama gulin.)\n"
    )


def yorumla(girdi: str | None = None) -> str:
    print("Kurul toplanıyor...")
    time.sleep(0.6)
    print("Evraklar tasiniyor...")
    time.sleep(0.4)
    print("Murekkep kontrol ediliyor...")
    time.sleep(0.3)

    sekil = girdi.strip() if girdi and girdi.strip() else random.choice(SEKILLER)
    karar = random.choice(KARARLAR)
    guven = random.randint(11, 97)

    rapor = (
        f"\nT.C. BULUT SEKLI YORUMLAMA KURULU\n"
        f"Tutanak No: {random.randint(1000, 9999)}/{datetime.now().year}\n"
        f"Tarih: {datetime.now().isoformat(timespec='seconds')}\n"
        f"Gozlemlenen sekil: {sekil}\n"
        f"Resmi yorum: Bu, buyuk ihtimalle {sekil}dir.\n"
        f"Kurul karari: {karar}\n"
        f"Bilimsel guven: %{guven}\n"
        f"Not: Bu karar temyiz edilemez. Cunku bulut kacti.\n"
    )
    return rapor + damga()


def main() -> None:
    girdi = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    print(yorumla(girdi))


if __name__ == "__main__":
    main()
