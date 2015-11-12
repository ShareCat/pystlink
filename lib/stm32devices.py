#   : by PART_NO/CORE
#       : by DEV_ID
#           : by flash_size and or device type

DEVICES = [
    {
        'part_no': 0xc20,
        'core': 'CortexM0',
        'idcode_reg': 0x40015800,
        'devices': [
            {
                'dev_id': 0x440,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F030x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F051x4', 'flash_size':   16, 'sram_size':   8, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F051x6', 'flash_size':   32, 'sram_size':   8, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F051x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F058x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  0, 'freq':  48},
                ],
            },
            {
                'dev_id': 0x442,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F030xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F091xB', 'flash_size':  128, 'sram_size':  32, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F091xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F098xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  48},
                ],
            },
            {
                'dev_id': 0x444,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F030x4', 'flash_size':   16, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F030x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F031x4', 'flash_size':   16, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F031x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F038x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                ],
            },
            {
                'dev_id': 0x445,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F042x4', 'flash_size':   16, 'sram_size':   6, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F042x6', 'flash_size':   32, 'sram_size':   6, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F048x6', 'flash_size':   32, 'sram_size':   6, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F070x6', 'flash_size':   32, 'sram_size':   6, 'eeprom_size':  0, 'freq':  48},
                ],
            },
            {
                'dev_id': 0x448,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F070xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F071x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F071xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F072x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F072xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F078xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                ],
            },
        ],
    },
    {
        'part_no': 0xc60,
        'core': 'CortexM0+',
        'idcode_reg': 0x40015800,
        'devices': [
            {
                'dev_id': 0x425,  # category 2
                'flash_size_reg': 0x1ff8007c,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L031x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  1, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x417,  # category 3
                'flash_size_reg': 0x1ff8007c,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L051x6', 'flash_size':   32, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L051x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L052x6', 'flash_size':   32, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L052x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L053x6', 'flash_size':   32, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L053x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L062x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L063x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x447,  # category 5
                'flash_size_reg': 0x1ff8007c,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L071xZ', 'flash_size':  192, 'sram_size':  20, 'eeprom_size':  6, 'freq':  32},
                    {'type': 'STM32L072xZ', 'flash_size':  192, 'sram_size':  20, 'eeprom_size':  6, 'freq':  32},
                    {'type': 'STM32L073xZ', 'flash_size':  192, 'sram_size':  20, 'eeprom_size':  6, 'freq':  32},
                    {'type': 'STM32L083xZ', 'flash_size':  192, 'sram_size':  20, 'eeprom_size':  6, 'freq':  32},
                ],
            },
        ],
    },
    {
        'part_no': 0xc23,
        'core': 'CortexM3',
        'idcode_reg': 0xE0042000,
        'devices': [
            {
                'dev_id': 0x410,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F101x8', 'flash_size':   64, 'sram_size':  10, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F101xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F102x8', 'flash_size':   64, 'sram_size':  10, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F102xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F103x8', 'flash_size':   64, 'sram_size':  20, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F103xB', 'flash_size':  128, 'sram_size':  20, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x411,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F205xB', 'flash_size':  128, 'sram_size':  64, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F205xC', 'flash_size':  256, 'sram_size':  96, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F205xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F205xF', 'flash_size':  768, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F205xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F207xC', 'flash_size':  256, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F207xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F207xF', 'flash_size':  768, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F207xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F215xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F215xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F217xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                    {'type': 'STM32F217xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq': 120},
                ],
            },
            {
                'dev_id': 0x412,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F101x4', 'flash_size':   16, 'sram_size':   4, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F101x6', 'flash_size':   32, 'sram_size':   6, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F102x4', 'flash_size':   16, 'sram_size':   4, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F102x6', 'flash_size':   32, 'sram_size':   6, 'eeprom_size':  0, 'freq':  48},
                    {'type': 'STM32F103x4', 'flash_size':   16, 'sram_size':   6, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F103x6', 'flash_size':   32, 'sram_size':  10, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x414,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F101xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F101xD', 'flash_size':  384, 'sram_size':  48, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F101xE', 'flash_size':  512, 'sram_size':  48, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F103xC', 'flash_size':  256, 'sram_size':  48, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F103xD', 'flash_size':  384, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F103xE', 'flash_size':  512, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x416,
                'flash_size_reg': 0x1ff8004c,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L100x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L100x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L100xB', 'flash_size':  128, 'sram_size':  10, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L151x6', 'flash_size':   32, 'sram_size':  10, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L151x8', 'flash_size':   64, 'sram_size':  10, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L151xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152x6', 'flash_size':   32, 'sram_size':  10, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152x8', 'flash_size':   64, 'sram_size':  10, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152xB', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  4, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x418,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F105x8', 'flash_size':   64, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F105xB', 'flash_size':  128, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F105xC', 'flash_size':  256, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F107xB', 'flash_size':  128, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F107xC', 'flash_size':  256, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x420,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (1024, ),
                'devices': [
                    {'type': 'STM32F100x4', 'flash_size':   16, 'sram_size':   4, 'eeprom_size':  0, 'freq':  24},
                    {'type': 'STM32F100x6', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  0, 'freq':  24},
                    {'type': 'STM32F100x8', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  0, 'freq':  24},
                    {'type': 'STM32F100xB', 'flash_size':  128, 'sram_size':   8, 'eeprom_size':  0, 'freq':  24},
                ],
            },
            {
                'dev_id': 0x422,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F302xB', 'flash_size':  128, 'sram_size':  32, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F302xC', 'flash_size':  256, 'sram_size':  40, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F303xB', 'flash_size':  128, 'sram_size':  40, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F303xC', 'flash_size':  256, 'sram_size':  48, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F358xC', 'flash_size':  256, 'sram_size':  48, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x427,
                'flash_size_reg': 0x1ff800cc,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L100xC', 'flash_size':  256, 'sram_size':  16, 'eeprom_size':  8, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x428,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F100xC', 'flash_size':  256, 'sram_size':  24, 'eeprom_size':  0, 'freq':  24},
                    {'type': 'STM32F100xD', 'flash_size':  384, 'sram_size':  32, 'eeprom_size':  0, 'freq':  24},
                    {'type': 'STM32F100xE', 'flash_size':  512, 'sram_size':  32, 'eeprom_size':  0, 'freq':  24},
                ],
            },
            {
                'dev_id': 0x429,
                'flash_size_reg': 0x1ff8004c,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L100x6-A', 'flash_size':   32, 'sram_size':   4, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L100x8-A', 'flash_size':   64, 'sram_size':   8, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L100xB-A', 'flash_size':  128, 'sram_size':  16, 'eeprom_size':  2, 'freq':  32},
                    {'type': 'STM32L151x6-A', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L151x8-A', 'flash_size':   64, 'sram_size':  32, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L151xB-A', 'flash_size':  128, 'sram_size':  32, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152x6-A', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152x8-A', 'flash_size':   64, 'sram_size':  32, 'eeprom_size':  4, 'freq':  32},
                    {'type': 'STM32L152xB-A', 'flash_size':  128, 'sram_size':  32, 'eeprom_size':  4, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x430,
                'flash_size_reg': 0x1ffff7e0,
                'flash_driver': 'STM32FPXL',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F101xF', 'flash_size':  768, 'sram_size':  80, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F101xG', 'flash_size': 1024, 'sram_size':  80, 'eeprom_size':  0, 'freq':  36},
                    {'type': 'STM32F103xF', 'flash_size':  768, 'sram_size':  96, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F103xG', 'flash_size': 1024, 'sram_size':  96, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x432,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F373x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F373xB', 'flash_size':  128, 'sram_size':  24, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F373xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F378xC', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x436,
                'flash_size_reg': 0x1ff800cc,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L151xC',   'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L151xC-A', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L151xD',   'flash_size':  384, 'sram_size':  48, 'eeprom_size': 12, 'freq':  32},
                    {'type': 'STM32L152xC',   'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L152xC-A', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L152xD',   'flash_size':  384, 'sram_size':  48, 'eeprom_size': 12, 'freq':  32},
                    {'type': 'STM32L162xC',   'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L162xC-A', 'flash_size':  256, 'sram_size':  32, 'eeprom_size':  8, 'freq':  32},
                    {'type': 'STM32L162xD',   'flash_size':  384, 'sram_size':  48, 'eeprom_size': 12, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x437,
                'flash_size_reg': 0x1ff800cc,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L151xD-X', 'flash_size':  384, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                    {'type': 'STM32L151xE',   'flash_size':  512, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                    {'type': 'STM32L152xD-X', 'flash_size':  384, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                    {'type': 'STM32L152xE',   'flash_size':  512, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                    {'type': 'STM32L162xD-X', 'flash_size':  384, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                    {'type': 'STM32L162xE',   'flash_size':  512, 'sram_size':  80, 'eeprom_size': 16, 'freq':  32},
                ],
            },
            {
                'dev_id': 0x438,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F303x6', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F303x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F328x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F334x4', 'flash_size':   16, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F334x6', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F334x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x439,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F301x6', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F301x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F302x6', 'flash_size':   32, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F302x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F318x8', 'flash_size':   64, 'sram_size':  16, 'eeprom_size':  0, 'freq':  72},
                ],
            },
            {
                'dev_id': 0x446,
                'flash_size_reg': 0x1ffff7cc,
                'flash_driver': 'STM32FP',
                'erase_sizes': (2048, ),
                'devices': [
                    {'type': 'STM32F302xD', 'flash_size':  384, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F302xE', 'flash_size':  512, 'sram_size':  64, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F303xD', 'flash_size':  384, 'sram_size':  80, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F303xE', 'flash_size':  512, 'sram_size':  80, 'eeprom_size':  0, 'freq':  72},
                    {'type': 'STM32F398xE', 'flash_size':  512, 'sram_size':  80, 'eeprom_size':  0, 'freq':  72},
                ],
            },
        ],
    },
    {
        'part_no': 0xc24,
        'core': 'CortexM4',
        'idcode_reg': 0xE0042000,
        'devices': [
            {
                'dev_id': 0x413,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F405xE', 'flash_size':  512, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F405xG', 'flash_size': 1024, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F407xE', 'flash_size':  512, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F407xG', 'flash_size': 1024, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F415xG', 'flash_size': 1024, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F417xE', 'flash_size':  512, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                    {'type': 'STM32F417xG', 'flash_size': 1024, 'sram_size': 192, 'eeprom_size':  0, 'freq': 168},
                ],
            },
            {
                'dev_id': 0x415,
                'flash_size_reg': 0x1ff75e0,
                'flash_driver': None,
                'erase_sizes': None,
                'devices': [
                    {'type': 'STM32L476xC', 'flash_size':  256, 'sram_size': 128, 'eeprom_size':  0, 'freq':  80},
                    {'type': 'STM32L476xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq':  80},
                    {'type': 'STM32L476xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq':  80},
                    {'type': 'STM32L486xG', 'flash_size': 1024, 'sram_size': 128, 'eeprom_size':  0, 'freq':  80},
                ],
            },
            {
                'dev_id': 0x419,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F427xG', 'flash_size': 1024, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F427xI', 'flash_size': 2048, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F429xE', 'flash_size':  512, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F429xG', 'flash_size': 1024, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F429xI', 'flash_size': 2048, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F437xG', 'flash_size': 1024, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F437xI', 'flash_size': 2048, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F439xG', 'flash_size': 1024, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F439xI', 'flash_size': 2048, 'sram_size': 256, 'eeprom_size':  0, 'freq': 180},
                ],
            },
            {
                'dev_id': 0x421,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F446xC', 'flash_size':  256, 'sram_size': 128, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F446xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 180},
                ],
            },
            {
                'dev_id': 0x423,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F401xB', 'flash_size':  128, 'sram_size':  64, 'eeprom_size':  0, 'freq':  84},
                    {'type': 'STM32F401xC', 'flash_size':  256, 'sram_size':  64, 'eeprom_size':  0, 'freq':  84},
                ],
            },
            {
                'dev_id': 0x431,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F411xC', 'flash_size':  256, 'sram_size': 128, 'eeprom_size':  0, 'freq': 100},
                    {'type': 'STM32F411xE', 'flash_size':  512, 'sram_size': 128, 'eeprom_size':  0, 'freq': 100},
                ],
            },
            {
                'dev_id': 0x433,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F401xD', 'flash_size':  384, 'sram_size':  96, 'eeprom_size':  0, 'freq':  84},
                    {'type': 'STM32F401xE', 'flash_size':  512, 'sram_size':  96, 'eeprom_size':  0, 'freq':  84},
                ],
            },
            {
                'dev_id': 0x434,
                'flash_size_reg': 0x1fff7a22,
                'flash_driver': 'STM32FS',
                'erase_sizes': (16*1024, 16*1024, 16*1024, 16*1024, 64*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, 128*1024, ),
                'devices': [
                    {'type': 'STM32F469xE', 'flash_size':  512, 'sram_size': 384, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F469xG', 'flash_size': 1024, 'sram_size': 384, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F469xI', 'flash_size': 2048, 'sram_size': 384, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F479xG', 'flash_size': 1024, 'sram_size': 384, 'eeprom_size':  0, 'freq': 180},
                    {'type': 'STM32F479xI', 'flash_size': 2048, 'sram_size': 384, 'eeprom_size':  0, 'freq': 180},
                ],
            },
        ],
    },
    {
        'part_no': 0xc27,
        'core': 'CortexM7',
        'idcode_reg': 0xE0042000,
        'devices': [
            {
                'dev_id': 0x449,
                'flash_size_reg': 0x1ff0f442,
                'flash_driver': 'STM32FS',
                'erase_sizes': (32*1024, 32*1024, 32*1024, 32*1024, 128*1024, 256*1024, 256*1024, 256*1024, ),
                'devices': [
                    {'type': 'STM32F745xE', 'flash_size':  512, 'sram_size': 320, 'eeprom_size':  0, 'freq': 216},
                    {'type': 'STM32F745xG', 'flash_size': 1024, 'sram_size': 320, 'eeprom_size':  0, 'freq': 216},
                    {'type': 'STM32F746xE', 'flash_size':  512, 'sram_size': 320, 'eeprom_size':  0, 'freq': 216},
                    {'type': 'STM32F746xG', 'flash_size': 1024, 'sram_size': 320, 'eeprom_size':  0, 'freq': 216},
                    {'type': 'STM32F756xG', 'flash_size': 1024, 'sram_size': 320, 'eeprom_size':  0, 'freq': 216},
                ]
            },
        ]
    },
]
