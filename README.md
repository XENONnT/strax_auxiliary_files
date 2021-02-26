# strax_auxiliary_files
[![Pytest](https://github.com/XENONnT/strax_auxiliary_files/actions/workflows/test_package.yml/badge.svg)](https://github.com/XENONnT/strax_auxiliary_files/actions/workflows/test_package.yml)

Files needed for running strax on XENON data

# How to use
Before if uploading any data please update the table below with a short description of the file and preferably a link to a wiki note where it is discussed.a

# ./strax_files
| File-name                     | Short description             |Used for       | Link      |
| ---------                     | ---------                     | ---------     |---------  |
|`elipe.npy`                    |1T electron livetimes          |`straxen`      |           |
|`filters_per_chan.npy`         |1T pulse filters per channel   |`straxen` 1T   |[link](https://xe1t-wiki.lngs.infn.it/doku.php?id=xenon:xenonnt:analysis:waveforms_team:single_pe_deconvolution) |
|`pmt_positions_xenonnt.csv`    |nT PMT positions               |`straxen` 1T   |[link](https://xe1t-wiki.lngs.infn.it/doku.php?id=xenon:xenonnt:analysis:coordinate_system#analysis_and_pmt_coordinate_system) |
|`remapped_channels_....csv`    |(see link)                     |`straxen` nT   |[link](https://xe1t-wiki.lngs.infn.it/doku.php?id=xenon:xenonnt:dsg:daq:sector_swap) |
|`strax_test_data.tar`          |Ancient strax test data        |`straxen`      |           |
|`strax_test_data_straxv0.9.tar`|Straxen test data              |`straxen`      |           |
|`to_pe.npy`                    |1T to pe per running           |`straxen` 1T   |           |
|`XENON1T_..._20171217_sr0.h5`  |SR0 NN                         |`straxen` 1T   |?          |
|`XENON1T_..._20171217_sr1.h5`  |SR1 NN                         |`straxen` 1T   |?          |
|`XENON1T_..._20171217_sr1_reformatted.json` |SR1 NN            |`straxen` 1T   |?          |

# ./sim_files
| File-name                     | Short description             |Used for       | Link      |
| ---------                     | ---------                     | ---------     |---------  |
|`170203_0850_00_small.npz`     |                               |`wfsim`        |           |
|`ele_after_pulse.npy`          |1T el. afterpulse template     |`wfsim`        |           |
|`fax_config.json`              |wfsim conf placeholder         |`wfsim`        |           |
|`fax_config_1t.json`           |wfsim 1T conf                  |`wfsim`        |           |
|`mlp_model.h5`                 |nT NN placeholder              |`straxen` nT   |           |
|`mlp_model.json`               |nt NN placeholder              |`straxen` nT   |           |
|`placeholder_map.json`         |?                              |`?`            |           |
|`x1t_noise_170203_0850_....npz`|1T Noise template              |`wfsim`        |           |
|`x1t_pmt_afterpulse_config.pkl.gz`|1T pmt afterpulse template  |`wfsim`        |           |
|`x1t_se_afterpulse_delaytime.pkl.gz`|1T single electron afterpulse|`wfsim`     |           |
|`XENON1T_effective_diffusion_SR1.pkl`|1T diffusion model       |`wfsim`        |           |
|`XENON1T_FDC_SR1_data_dr....gz`|1T field distortion correction |`wfsim`        |           |
|`XENON1T_s1_xyz_ly_kr8....json`|1T light-yield map             |`wfsim`        |           |
|`XENON1T_s1_xyz_patterns....gz`|1T iterpolation map            |`wfsim`        |           |
|`XENON1T_s2_xy_ly_SR1_v2.2.json`|1T S2 light-yield map         |`wfsim`        |           |
|`XENON1T_s2_xy_patterns_....gz`|1T pattern map                 |`wfsim`        |           |
|`XENON1T_spe_distributions.csv`|1T single photonelectron distributions |`wfsim`|           |

# This repo is structured as a package. To interact:
## Install:
```bash
git clone https://github.com/XENONnT/strax_auxiliary_files
cd strax_auxiliary_files
python setup.py develop
```

## Open files
These are some examples of how to interact with the package.

### Example 1. Open a simulation file
Let's see how we can interact with the package. Below is an example of how we can open a simulation file.
```python
import straxauxfiles
# Let's see what kind of simulation files we have
print(straxauxfiles.list_sim_files())
# Let's load the fax_config_nt and open it as a dictionary
config = straxauxfiles.get_sim_file('fax_config.json', fmt='json')
# We can now treat it as a dictionary
print(config.keys())
```

### Example 3. Open a strax file
Let's see how we can interact with the package. Below is an example of how we can open a simulation file.
```python
import straxauxfiles
# Let's see what kind of strax files we have
print(straxauxfiles.list_strax_files())
# Let's load the fax_config_nt and open it as a dictionary
print(straxauxfiles.get_strax_file('elife.npy', fmt='npy'))
```

### Example 2. Locate all the files in this auxiliary repo
Let's see how we can interact with the package. Below is an example of how we can open a simulation file.
```python
import straxauxfiles
# Let's see what kind of files we have
print(straxauxfiles.list_aux_files())
# Let's make a a dictionary of the paths of each of the files.
my_files = {f: straxauxfiles.get_abspath(f) for f in straxauxfiles.list_aux_files()}
# Print the dictionary
print(my_files)
