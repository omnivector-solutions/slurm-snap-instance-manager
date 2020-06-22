# Slurm Snap Manager
This code provides a reuasable way to facilitate slurm snap lifecycle operations.

```python
class SlurmCharm(CharmBase):
    def __init__(self, *args):
        super().__init__(*args)

        self.slurm_snap = SlurmSnapInstanceManager(self, "slurmdbd")

    def _on_install(self, event):
	self.slurm_snap.install()
```

##### Copyright
* OmniVector Solutions <admin@omnivector.solutions>
