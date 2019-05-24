# pyHardware
a rewrite of python-hwinfo to support python3

To get dmidecode info, you will need sudo/root, as well as the related package that installs ```dmidecode``` for your Linux Distribution.

```python
from hw import dmidecode_reader

dmidcode_data=dmidecode_reader.getDmidecode().parsed
#get bios info from data
bios_info={i:dmidecode_data[i] for i in dmidecode_data.keys() if i.endswith('bios_info')}
```

To get cpu information you will need the related package that installs ```lscpu```.

```python
from hw import cpu_reader
cpu_data=cpu_reader.getCpu().parsed
```

To get PCI information you will need the related package that installs ```lspci```.

```python
from hw import lspci_reader
lspci_data=lspci_reader.getLspci().parsed
```

The resulting data from each generated will be a dictionary of the desired data.
