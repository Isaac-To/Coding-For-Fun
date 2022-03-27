import os
def h_cmd(cmd):
    os.system(f'{cmd}>/dev/null 2>&1')
class ui():
    def dmet(prompt):
        print(f'[✔️] {prompt} has been detected!')
    def dfail(prompt):
        print(f'[✖️] {prompt} was not detected!')
    def app(prompt):
        print(f'[+] Applied {prompt}')
class nv():
    def smi(GPU, arg):
        h_cmd(f'nvidia-smi -i {GPU} --{arg}')
    def set(GPU, arg):
        h_cmd(f'nvidia-settings -a [gpu:{GPU}]/{arg}')
    def set_coolbits(arg):
        if nv.nvidia():
            try:
                #enable GPU overclocking
                h_cmd(f'nvidia-xconfig --cool-bits={arg}')
                f = open('/usr/share/X11/xorg.conf.d/10-nvidia.conf', 'w')
                f.write('Section "OutputClass"\n\tIdentifier "nvidia"\n\tMatchDriver "nvidia-drm"\n\tDriver "nvidia"\n\tOption "AllowEmptyInitialConfiguration"\n\tOption "Coolbits" "12"\n\tModulePath "/usr/lib/x86_64-linux-gnu/nvidia/xorg"\nEndSection')
                f.close()
                input('Press [enter] to reboot')
                h_cmd('reboot')
            except:
                ui.dfail('Coolbits')
        else:
            #if a NVIDIA GPU is not detected
            ui.dfail('A NVIDIA GPU')
    def coolbits(arg):
        f = open('/etc/X11/xorg.conf')
        xorg = f.read()
        if f'"Coolbits" "{arg}"' in xorg:
            return True
        f.close()
        f = open('/usr/share/X11/xorg.conf.d/10-nvidia.conf')
        xorg = f.read()
        if f'"Coolbits" "{arg}"' in xorg:
            return True
        return False
    def nvidia():
        f = open('/etc/X11/xorg.conf')
        xorg = f.read()
        if 'NVIDIA' in xorg:
            return True
        return False
    class core():
        def set_clk(GPU, GPU_CLK):
            nv.set(GPU, f'GPUGraphicsClockOffsetAllPerformanceLevels={GPU_CLK}')
            ui.app(f'{GPU_CLK}MHz GPU offset')
        def set_pwr(GPU, GPU_PWR):
            nv.smi(GPU, f'power-limit={GPU_PWR}')
            ui.app(f'{GPU_PWR}w limit')
        def set_state(GPU, MODE):
            nv.set(GPU, f'GpuPowerMizerMode={MODE}')
            ui.app(f'P{MODE-1} state')
        def set_compute(GPU, choice):
            nv.smi(GPU, f'compute-mode={choice}')
            ui.app(f'Compute Mode = {choice}')
    class mem():
        def set_clk(GPU, MEM_CLK):
            nv.set(GPU, f'GPUMemoryTransferRateOffsetAllPerformanceLevels={MEM_CLK}')
            ui.app(f'{MEM_CLK}MHz MEM offset')
    class fan():
        def set_spd(GPU, per):
            nv.set(GPU, f'GPUFanControlState=1 -a [fan-0]/GPUTargetFanSpeed={per}')
            ui.app(f'fan speed {per}%')