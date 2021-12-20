import sys
from copy import deepcopy
from functools import reduce
from operator import mul
import pdb

def load_input(text_file):
    # Helper function to load in the test text file and convert to
    # string of 1s and 0s for processing
    with open(text_file,'r') as infile:
        input_string = infile.readline()
    out_string = ""
    for inchar in input_string.rstrip():
        out_string += format(int(inchar,16),'04b')
    return out_string

class Packetizer(object):
    """Packetizer class used to process input binary string, and create
    the 
    
    """
    def __init__(self, input_str):
        self.input_str = input_str
        self.packets = []
        while len(self.input_str):
            if '1' not in self.input_str:
                self.input_str = ''
                break
            packet = {}
            packet['version'] = int(self.input_str[:3],2)
            packet['typeID'] =  int(self.input_str[3:6],2)
            packet['payload'] = self._process_payload(packet['typeID'])
            self.packets.append(packet)
    
    # Set accumulator operations at the class level
    accumulators = {0: sum,
                    1: lambda x: reduce(mul, x),
                    2: min,
                    3: max,
                    4: lambda x: x['payload'],
                    5: lambda x: 1 if x[0]>x[1] else 0,
                    6: lambda x: 1 if x[0]<x[1] else 0,
                    7: lambda x: 1 if x[0]==x[1] else 0
                }

    def _process_payload(self, typeID):
        if typeID==4:
            return self._process_literal_value()
        else:
            return self._process_operator()

    def _process_literal_value(self):
        payload_str = ''
        for istart in range(6,len(self.input_str),5):
            flag = int(self.input_str[istart])
            payload_str += self.input_str[istart+1:istart+5]
            if not flag:
                break
        # discard the processed string bits (inc. the nearest 4-bit word)
        #nwords, rem = divmod(istart+5,4)
        #nwords += int(bool(rem))
        #self.input_str = self.input_str[4*nwords:]
        self.input_str = self.input_str[istart+5:]
        return int(payload_str,2)

    def _process_operator(self):
        length_typeID = int(self.input_str[6])
        if length_typeID:
            retpackets = []
            n_subpackets = int(self.input_str[7:18],2)
            self.input_str = self.input_str[18:]
            for i in range(n_subpackets):
                packet = {}
                packet['version'] = int(self.input_str[:3],2)
                packet['typeID'] =  int(self.input_str[3:6],2)
                packet['payload'] = self._process_payload(packet['typeID'])
                retpackets.append(packet)
            return retpackets
        else:
            nbits = int(self.input_str[7:22],2)
            tmpstr = deepcopy(self.input_str[22:22+nbits])
            self.input_str = self.input_str[22+nbits:]
            tmp_packetizer = Packetizer(tmpstr)
            return tmp_packetizer.packets

            
def sum_version_numbers(packetlist):
    sum = 0
    for packet in packetlist:
        if isinstance(packet['payload'],list):
            sum += sum_version_numbers(packet['payload'])
        sum += packet['version']
    return sum

def run_version_test(test_file,expected_output):
    print(f"Running test file {test_file} ...",end="")
    input_string = load_input(test_file)
    packetizer = Packetizer(input_string)
    output = sum_version_numbers(packetizer.packets)
    assert(output==expected_output)
    print(" Passed!")

def accumulate_packet(packet):
    if packet['typeID'] == 4:
        return packet['payload']
    else:
        operation = Packetizer.accumulators[packet['typeID']]
        subpackets = [accumulate_packet(subpacket) for subpacket in packet['payload']]
        return operation(subpackets)

def run_accumulate_test(test_file,expected_output):
    print(f"Running test file {test_file} ...",end="")
    input_string = load_input(test_file)
    packetizer = Packetizer(input_string)
    accumulated = accumulate_packet(packetizer.packets[0])
    assert(accumulated==expected_output)
    print(" Passed!")


if __name__=="__main__":
    run_version_test("test_A_sixteen.txt",16)
    run_version_test("test_B_sixteen.txt",12)
    run_version_test("test_C_sixteen.txt",23)
    run_version_test("test_D_sixteen.txt",31)


    run_accumulate_test("test_E_sixteen.txt",3)
    run_accumulate_test("test_F_sixteen.txt",54)
    run_accumulate_test("test_G_sixteen.txt",7)
    run_accumulate_test("test_H_sixteen.txt",9)
    run_accumulate_test("test_I_sixteen.txt",1)
    run_accumulate_test("test_J_sixteen.txt",0)
    run_accumulate_test("test_K_sixteen.txt",0)
    run_accumulate_test("test_L_sixteen.txt",1)
    run_accumulate_test("test_M_sixteen.txt",0)
    run_accumulate_test("test_N_sixteen.txt",192)
    run_accumulate_test("test_O_sixteen.txt",10000000000)
    run_accumulate_test("test_P_sixteen.txt",3)
    run_accumulate_test("test_Q_sixteen.txt",2)
    run_accumulate_test("test_R_sixteen.txt",2)

    input_string = load_input("input_sixteen.txt")
    packetizer = Packetizer(input_string)
    output_versions = sum_version_numbers(packetizer.packets)
    print(f"Sum of versions in puzzle input: {output_versions}")
    output_accumulation = accumulate_packet(packetizer.packets[0])
    print(f"Accumulation of packets in puzzle input: {output_accumulation}")

    

