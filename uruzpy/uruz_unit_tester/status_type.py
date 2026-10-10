# SPDX-License-Identifier: Uruz Open Commercial License (UOCL)-1.0
# Created: 2026-10-06
# Author: Uruz - Utku Ün (Kurt)
__version__ = "1.0.0"


from enum import Enum


class StatusType(Enum):
    SUCCESS = "[OK]"  # Başarı Durumu
    FAILURE = "[FAIL]"  # Başarısızlık Durumu
