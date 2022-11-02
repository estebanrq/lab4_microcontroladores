#!/bin/bash

echo "LAB 4 SETUP:"
echo "  > Creating link"
ln -sf libopencm3-examples-master/examples/stm32/f4/stm32f429i-discovery/spi/ src
echo "  > Going to source area"
cd src/
echo "  > make clean"
make clean
echo "  > make"
make
echo "  > Generating spi-mems.bin"
arm-none-eabi-objcopy -O binary spi-mems.elf spi-mems.bin
cd ..