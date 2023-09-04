import abc


class Device(abc.ABC):
    @abc.abstractmethod
    def is_enabled(self):
        pass

    @abc.abstractmethod
    def enable(self):
        pass

    @abc.abstractmethod
    def disable(self):
        pass

    @abc.abstractmethod
    def get_volume(self):
        pass

    @abc.abstractmethod
    def set_volume(self, volume: int):
        pass


class RemoteControl:
    # protected field device: Device
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


class TV(Device):
    MAX_VOLUME = 100

    def __init__(self):
        self.enabled: bool = False
        self.volume: int = 0

    def is_enabled(self):
        return self.enabled

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def get_volume(self):
        return self.volume

    def set_volume(self, volume: int):
        self.volume = min(volume, TV.MAX_VOLUME)


class Radio(Device):
    MAX_VOLUME = 30

    def __init__(self):
        self.volume: int = 0

    def is_enabled(self):
        return self.volume > 0

    def enable(self):
        if not self.is_enabled():
            self.volume = 5

    def disable(self):
        self.volume = 0

    def get_volume(self):
        return self.volume

    def set_volume(self, volume: int):
        self.volume = min(volume, TV.MAX_VOLUME)
