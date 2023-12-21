from smbus2 import SMBus
from time import sleep

class I2C():
    MASTER = 0
    SLAVE  = 1
    RETRY = 5

    def __init__(self, *args, **kargs):     
        super().__init__()
        self._bus = 1
        self._smbus = SMBus(self._bus)

    def _i2c_write_byte(self, addr, data):                      # i2C write function
        return self._smbus.write_byte(addr, data)

    def _i2c_write_byte_data(self, addr, reg, data):
        return self._smbus.write_byte_data(addr, reg, data)

    def _i2c_write_word_data(self, addr, reg, data):
        return self._smbus.write_word_data(addr, reg, data)

    def _i2c_write_i2c_block_data(self, addr, reg, data):
        return self._smbus.write_i2c_block_data(addr, reg, data)

    def _i2c_read_byte(self, addr):                             # i2C read functions
        return self._smbus.read_byte(addr)

    def _i2c_read_i2c_block_data(self, addr, reg, num):
        return self._smbus.read_i2c_block_data(addr, reg, num)

    def is_ready(self, addr):
        addresses = self.scan()
        if addr in addresses:
            return True
        else:
            return False

    def scan(self):                                             # scan available i2c devices
        cmd = "i2cdetect -y %s" % self._bus
        _, output = self.run_command(cmd)                       # run linux command and return the output of it

        outputs = output.split('\n')[1:]                        
        addresses = []
        for tmp_addresses in outputs:
            if tmp_addresses == "":
                continue
            tmp_addresses = tmp_addresses.split(':')[1]
            tmp_addresses = tmp_addresses.strip().split(' ')    # remove leading & trailing space, then split by space 
            for address in tmp_addresses:
                if address != '--':
                    addresses.append(int(address, 16))
        return addresses

    def send(self, send, addr, timeout=0):                      # sending data. `send`: data to be sent, `addr`: receiver's address 
        if isinstance(send, bytearray):
            data_all = list(send)
        elif isinstance(send, int):
            data_all = []
            d = "{:X}".format(send)
            d = "{}{}".format("0" if len(d)%2 == 1 else "", d)  
            # print(d)
            for i in range(len(d)-2, -1, -2):                   # taking two chars in each iteration from right to left 
                tmp = int(d[i:i+2], 16)                         # convert 2-digit decimal to hex
                # print(tmp)
                data_all.append(tmp)                            
            data_all.reverse()
        elif isinstance(send, list):
            data_all = send
        else:
            raise ValueError("send data must be int, list, or bytearray, not {}".format(type(send)))

        if len(data_all) == 1:                    
            data = data_all[0]
            self._i2c_write_byte(addr, data)
        elif len(data_all) == 2:                   
            reg = data_all[0]
            data = data_all[1]
            self._i2c_write_byte_data(addr, reg, data)
        elif len(data_all) == 3:                    
            reg = data_all[0]
            data = (data_all[2] << 8) + data_all[1]
            self._i2c_write_word_data(addr, reg, data)
        else:
            reg = data_all[0]
            data = list(data_all[1:])
            self._i2c_write_i2c_block_data(addr, reg, data)

    def recv(self, recv, addr=0x00, timeout=0):                 # receive data
        if isinstance(recv, int):                               # convert `recv` to bytearray
            result = bytearray(recv)
        elif isinstance(recv, bytearray):
            result = recv
        else:
            return False
        for i in range(len(result)):
            result[i] = self._i2c_read_byte(addr)
        return result

    def mem_write(self, data, addr, memaddr, timeout=5000, addr_size=8): # memaddr match to chn
        if isinstance(data, bytearray):
            data_all = list(data)
        elif isinstance(data, list):
            data_all = data
        elif isinstance(data, int):
            data_all = []
            data = "%x"%data
            if len(data) % 2 == 1:
                data = "0" + data
            # print(data)
            for i in range(0, len(data), 2):
                # print(data[i:i+2])
                data_all.append(int(data[i:i+2], 16))
        else:
            raise ValueError("memery write require arguement of bytearray, list, int less than 0xFF")
        # print(data_all)
        self._i2c_write_i2c_block_data(addr, memaddr, data_all)

    def mem_read(self, data, addr, memaddr, timeout=5000, addr_size=8):  # read data
        if isinstance(data, int):
            num = data
        elif isinstance(data, bytearray):
            num = len(data)
        else:
            return False
        result = bytearray(self._i2c_read_i2c_block_data(addr, memaddr, num))
        return result

    def readfrom_mem_into(self, addr, memaddr, buf):
        buf = self.mem_read(len(buf), addr, memaddr)
        return buf

    def writeto_mem(self, addr, memaddr, data):
        self.mem_write(data, addr, memaddr)

