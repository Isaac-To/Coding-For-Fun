'''
SET YOUR GPU CONFIGURATIONS HERE
By using this program, you agree that all damages which may arise from this program is solely result of your own actions.
cupogpu by Chisaku-Dev

Instructions:
1. Set your GPU configuration here:
'''
#Which GPU to apply the OC
GPU = 0
#How much power to give to the GPU (in terms of Watts)
PWR = 140
#How big is the GPU clock offset ex. in 1900 + 210 = 2110; 210 is the offset
GPU_CL = 150
#How big is the memory offset
MEM_CL = 680
#Set GPU to defined P mode
PSTATE = 0
#Set Fan Speed % (This is static) ex. FAN_SPD = 60 for 60% fan speed
FAN_SPD = None
#Computer mode (Enabling compute mode may help with computational intensive performance) 0/Default, 1/Exclusive_Thread, 2/Prohibited, 3/Exclusive_Process
COMPUTE = 0
'''
2. Save the file
3. Run the python program with to apply your settings:
    sudo python3 cupogpu.py

For multiple gpus: just make copies of this file (No need to duplicate cupapi) and adjust them individually
Be sure to assign the GPU number as to not overclock the wrong one.

For startup apply: just add to startup applications:
gnome-terminal -e "python3 /home/isaac/CupOC/cupogpu.py"
-----------------------------------------------------------
DO NOT MODIFY BELOW HERE UNLESS YOU KNOW WHAT YOU ARE DOING
'''
#ensure that Coolbits is activated
import cupapi as cup
if cup.nv.coolbits(12):
    cup.ui.dmet('Coolbits')
    cup.nv.smi(GPU, 'persistence-mode=1')
    cup.nv.core.set_pwr(GPU, PWR)
    cup.nv.core.set_clk(GPU, GPU_CL)
    cup.nv.mem.set_clk(GPU, MEM_CL)
    cup.nv.core.set_compute(GPU, COMPUTE)
    cup.nv.core.set_state(GPU, PSTATE + 1)
    if FAN_SPD != None:
        cup.nv.fan.set_spd(GPU, FAN_SPD)
    print('Applied all tweaks')
elif cup.nv.nvidia():
    cup.nv.set_coolbits(12)
