# Slurm Snap Manager
This code provides a reuasable way to facilitate slurm snap lifecycle operations.

```python
class SlurmCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)
	snap_mode = "all"
        self.slurm_snap = SlurmSnapInstanceManager(self, snap_mode)

    def _on_install(self, event):
	self.slurm_snap.install()

    def _on_start(self, event):
        self.slurm_snap.set_snap_mode()
```

if you are supplyng the mysql charm as the database or setting up your own slurm cluster to write custom configs
you can supply a dictionary object to be written to the slurm snap config file

```python
slurm_snap.write_config(dict_object)
```

##### Copyright
* OmniVector Solutions <admin@omnivector.solutions>
