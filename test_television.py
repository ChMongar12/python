import pytest
from television import *
class Test:
    def setup_method(self):
        self.tvl = Television()
    def teardown_method(self):
        del self.tvl
    def test__init(self):
        assert self.tvl.__str__() =="Power = False,Channel = 0,Volume = 0"
    def test__power(self):
        self.tvl.power()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 0"
        self.tvl.power()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"

    def test__mute(self):
        self.tvl.power()
        self.tvl.volume_up()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 1"
        self.tvl.mute()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 0"
        self.tvl.power()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"
        self.tvl.power()
        self.tvl.mute()
        self.tvl.power()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 1"
    def test__channel_up(self):
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"
        self.tvl.power()
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = True,Channel = 1,Volume = 0"
        self.tvl.channel_up()
        self.tvl.channel_up()
        self.tvl.channel_up()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 0"

    def test__channel_down(self):
        self.tvl.channel_down()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"
        self.tvl.power()
        self.tvl.channel_down()
        assert self.tvl.__str__() == "Power = True,Channel = 3,Volume = 0"


    def test__volume_up(self):
        self.tvl.volume_up()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"
        self.tvl.power()
        self.tvl.volume_up()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 1"
        self.tvl.mute()
        self.tvl.volume_up()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 2"
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_up()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 2"
    def test__volume_down(self):
        self.tvl.volume_down()
        assert self.tvl.__str__() == "Power = False,Channel = 0,Volume = 0"
        self.tvl.power()
        self.tvl.volume_up()
        self.tvl.volume_up()
        self.tvl.volume_down()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 1"
        self.tvl.volume_up()
        self.tvl.mute()
        self.tvl.volume_down()
        assert self.tvl.__str__() == "Power = True,Channel = 0,Volume = 1"


if __name__ == '__main__':
    pytest.main()
