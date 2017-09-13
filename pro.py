import Tkinter as tk
import ttk
from ttk import *

def replay_refresh():
	
	content_replay.pack_forget()
	wolf.pack_forget()
	lynx_wolf.pack_forget()
	replay_version_entry.pack_forget()
	
	content_label.pack_forget()
	version_label.pack_forget()
	team_label.pack_forget()
	quit_butt.pack_forget()
	cross_butt.config(state='active')
	cross_butt.deselect()
	xpr_butt.config(state='active')
	xpr_butt.deselect()
	rep_butt.config(state='active')
	rep_butt.deselect()
	dak_butt.config(state='active')
	dak_butt.deselect()
	v.set('L')
	replay_refresh_butt.pack_forget()
	copyed_to_clip.config(text='')
	

def replay_name():
	global replay_refresh_butt, copyed_to_clip, quit_butt
	if(team_var.get()=='10'):
		new_team='W'
		lynx_wolf.config(state='disabled')
		wolf.config(state='disabled')
	if(team_var.get()=='11'):
		new_team='L'
		lynx_wolf.config(state='disabled')
		wolf.config(state='disabled')
	replay_file_name='R_'+con_var.get()[:8]+'_'+new_team+'_'+'V'+replay_version_var.get()
	file_name_text=replay_file_name
	window.clipboard_clear()
	window.clipboard_append(file_name_text)
	window.update()
	copyed_to_clip=tk.Label(window, text="File Name Copyed to the Clipboard")
	copyed_to_clip.pack()
	replay_refresh_butt=tk.Button(window, text="Refresh", command=replay_refresh)
	replay_refresh_butt.pack(anchor=tk.W)
	quit_butt=tk.Button(window, text="Quit", command=quit)
	quit_butt.pack(anchor=tk.W)

def cross_refresh():
	cross_content_label.pack_forget()
	cross_content_entry.pack_forget()	
	cross_content_version_label.pack_forget()
	cross_content_version_entry.pack_forget()
	cross_submit.pack_forget()
	copyed_to_clip.config(text='')
	quit_butt.pack_forget()
	cross_butt.config(state='active')
	cross_butt.deselect()
	xpr_butt.config(state='active')
	xpr_butt.deselect()
	rep_butt.config(state='active')
	rep_butt.deselect()
	dak_butt.config(state='active')
	dak_butt.deselect()
	v.set('L')
	cross_refresh_butt.pack_forget()
	

def cross_name():
	global copyed_to_clip, cross_refresh_butt, quit_butt
	cross_text_name=cross_content_var.get()+'_DVCPRO_V'+cross_version_var.get()
	window.clipboard_clear()
	window.clipboard_append(cross_text_name)
	window.update()
	copyed_to_clip=tk.Label(window, text="File Name Copyed to the Clipboard")
	copyed_to_clip.pack()
	cross_refresh_butt=tk.Button(window, text="Refresh", command=cross_refresh)
	cross_refresh_butt.pack(anchor=tk.W)
	quit_butt=tk.Button(window, text="Quit", command=quit)
	quit_butt.pack(anchor=tk.W)


def callback1():
	global cross_content_var, cross_version_var, cross_content_label, cross_content_entry, cross_content_version_label, cross_content_version_entry, cross_submit
	cross_content_var=tk.StringVar()
	cross_version_var=tk.StringVar()
	cross_content_label=tk.Label(window, text='Content Name')
	cross_content_label.pack()
	cross_content_entry=tk.Entry(window, textvariable=cross_content_var)
	cross_content_entry.pack()
	cross_content_version_label=tk.Label(window, text='Version Number')
	cross_content_version_label.pack()
	cross_content_version_entry=tk.Entry(window, textvariable=cross_version_var)
	cross_content_version_entry.pack()
	cross_submit=tk.Button(window, text='Submit', command=cross_name)
	cross_submit.pack()

def callback3():
	global team_var, con_var, content_replay, wolf, lynx_wolf,replay_version_entry,replay_version_var,content_label,version_label,team_label
	team_var=tk.StringVar()
	con_var=tk.StringVar()
	replay_version_var=tk.StringVar()
	team_var.set('L')
	content_label=tk.Label(window, text='Content')
	content_label.pack()
	content_replay=tk.Entry(window, textvariable=con_var)
	content_replay.pack()
	version_label=tk.Label(window, text='Version')
	version_label.pack()
	replay_version_entry=tk.Entry(window, textvariable=replay_version_var)
	replay_version_entry.pack()
	
	team_label=tk.Label(window, text='Team')
	team_label.pack()
	wolf=tk.Radiobutton(window, text="Wolves", value=10, variable=team_var, command=replay_name)
	wolf.pack()
	lynx_wolf=tk.Radiobutton(window, text="Lynx", value=11, variable=team_var, command=replay_name)
	lynx_wolf.pack()
	
		
def disable_teams():
	wolves_butt.config(state='disabled')
	lynx_butt.config(state='disabled')
	neither_butt.config(state='disabled')
def add_duration():
	global dur_var, f, file_name_button, version_number, version_number_lab, duration_entry, duration_label
	animated_butt.config(state='disabled')
	static_butt.config(state='disabled')
	dur_var=tk.StringVar()
	duration_label=tk.Label(window, text="Duration (Seconds)")
	duration_label.pack()
	duration_entry=tk.Entry(window, textvariable=dur_var)
	duration_entry.pack()	
	f=tk.StringVar()
	version_number_lab=tk.Label(window, text="Version Number")
	version_number_lab.pack()
	version_number=tk.Entry(window,textvariable=f)
	version_number.pack()
	file_name_button=tk.Button(window, text="Submit", command=dak_create_name)
	file_name_button.pack()

def static_add_submit():
	global f, file_name_button, version_number_lab, version_number
	f=tk.StringVar()
	animated_butt.config(state='disabled')
	static_butt.config(state='disabled')
	version_number_lab=tk.Label(window, text="Version Number")
	version_number_lab.pack()
	version_number=tk.Entry(window,textvariable=f)
	version_number.pack()
	file_name_button=tk.Button(window, text="Submit", command=dak_create_name)
	file_name_button.pack()

def quit():
	window.quit()

def refresh():
	global destroy_list,f, file_name_button, version_number_lab, version_number
	
	w.pack_forget()
	w_2.pack_forget()
	wolves_butt.pack_forget()
	lynx_butt.pack_forget()
	neither_butt.pack_forget()
	file_name_button.pack_forget()
	version_number_lab.pack_forget()
	version_number.pack_forget()
	zone_info.pack_forget()
	input_info.pack_forget()
	quit_butt.pack_forget()
	refresh_butt.pack_forget()
	static_butt.pack_forget()
	animated_butt.pack_forget()
	content_example.pack_forget()
	content_content.pack_forget()
	content_name.pack_forget()
	display_info.pack_forget()
	team_info.pack_forget()
	copyed_to_clip.config(text='')
	cross_butt.config(state='active')
	cross_butt.deselect()
	xpr_butt.config(state='active')
	xpr_butt.deselect()
	rep_butt.config(state='active')
	rep_butt.deselect()
	dak_butt.config(state='active')
	dak_butt.deselect()
	v.set('L')
	duration_label.pack_forget()
	duration_entry.pack_forget()
	
def dak_create_name():
	global quit_butt, refresh_butt,copyed_to_clip
	con_name=content_text.get()
	zone_name=variable.get()
	display_name=variable_2.get()
	version=f.get()
	team=a.get()
	duration=b.get()
	if(team=='5'):
		team='W1617'
	if(team=='6'):
		team='L17'
	if(team=='7'):
		team='Neither'	
	if(duration=='8'):
		duration='static'
	if(duration=='9'):
		duration='animated'+dur_var.get()	
	
	text=zone_name+"_"+display_name+"_"+con_name+"_"+version+"_"+team+"_"+duration+"_V"+version
	
	window.clipboard_clear()
	window.clipboard_append(text)
	window.update()
	copyed_to_clip=tk.Label(window, text="File Name Copyed to the Clipboard")
	copyed_to_clip.pack()
	
	quit_butt=tk.Button(window, text="Quit", command=quit)
	quit_butt.pack(anchor=tk.W)
	
	refresh_butt=tk.Button(window, text="Refresh", command=refresh)
	refresh_butt.pack(anchor=tk.W)
	
def display_opt(value):
	global content_text,zone_name, display_name, version, variable, variable_2,f,a,b,xpr_butt, wolves_butt, neither_butt, lynx_butt,animated_butt, static_butt, w_2, content_name, content_content, content_example, display_info, team_info
	
	if(variable.get()=='Fascia'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["Fullscreen", "Sideline", "Endzone"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Corner Boards'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Tables'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Stanchion'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Upper Voms'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["All"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='PE Voms'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["North", "South"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Top Stats'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["Fullscreen", "Top Strip", "Bottom Strip"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Underbelly Stats'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["Fullscreen", "Single"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Ring'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='Ticket Booth'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=["Fullscreen", "Counter"]
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='6th Street Marquee'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()
		
	if(variable.get()=='7th Street Marquee'):
		display_info=tk.Label(window, text="Display: ")
		display_info.pack(anchor=tk.W)
		OPTIONS_2=['']
		w_2=tk.OptionMenu(window, variable_2, *OPTIONS_2)
		w_2.pack()

	a=tk.StringVar()
	a.set("K")
	team_info=tk.Label(window, text="Team")
	team_info.pack(anchor=tk.W)
	wolves_butt=tk.Radiobutton(window, text="Wolves", variable=a, value=5, command=disable_teams)
	wolves_butt.pack(anchor=tk.W)
	lynx_butt=tk.Radiobutton(window, text="Lynx",variable=a, value=6,command=disable_teams)
	lynx_butt.pack(anchor=tk.W)
	neither_butt=tk.Radiobutton(window, text="Neither",variable=a, value=7,command=disable_teams)
	neither_butt.pack(anchor=tk.W)
	content_text=tk.StringVar()
	content_name=tk.Label(window,text="Content Name")
	content_name.pack(anchor=tk.W)
	content_content=tk.Entry(window,textvariable=content_text)
	content_content.pack(anchor=tk.W)
	content_example=tk.Label(window, text="ex. Sprite, Lynx Foundation, Clip")
	content_example.pack(anchor=tk.W)
	
	b=tk.StringVar()
	b.set("P")
	static_butt=tk.Radiobutton(window, text="Static", variable=b, value=8, command=static_add_submit)
	static_butt.pack(anchor=tk.W)
	animated_butt=tk.Radiobutton(window, text="Animated",variable=b, value=9, command=add_duration)
	animated_butt.pack(anchor=tk.W)
	
def dak_callback():
	global content_text,zone_name, display_name, version, variable, variable_2,f,a,b,xpr_butt,w, input_info, zone_info
	cross_butt.config(state='disabled')
	xpr_butt.config(state='disabled')
	rep_butt.config(state='disabled')
	dak_butt.config(state='disabled')
	input_info=tk.Label(window, text="Input Info")
	input_info.pack()
	zone_info=tk.Label(window, text="Zone: ")
	zone_info.pack(anchor=tk.W)
	OPTIONS=["Fascia", "Corner Boards", "Tables", "Stanchion", "Upper Voms", "PE Voms", "Top Stats", "Underbelly Stats", "Ring", "Ticket Booth", "6th Street Marquee","7th Street Marquee"]
	variable=tk.StringVar(window)
	variable.set('')
	w=tk.OptionMenu(window, variable, *OPTIONS, command=display_opt)
	w.pack()
	variable_2=tk.StringVar(window)
	variable_2.set('')

def callback2():
	global xpr_content_var, xpr_content_label, xpr_content_entry, xpr_display_label, xpr_display_var, xpr_display_options, xpr_seq_var, xpr_seq_label, xpr_seq_entry, xpr_loop_lab, xpr_loop_var, play_once, play_loop
	xpr_content_var=tk.StringVar()
	xpr_content_label=tk.Label(window, text='Content Name')
	xpr_content_label.pack()
	
	xpr_content_entry=tk.Entry(window, textvariable=xpr_content_var)
	xpr_content_entry.pack()
	xpr_display_label=tk.Label(window, text='Display')
	xpr_display_label.pack()
	
	OPTIONS=['FTO', 'TS', 'FS', 'L3'] 
	xpr_display_var=tk.StringVar(window)
	xpr_display_var.set('')
	xpr_display_options=tk.OptionMenu(window,xpr_display_var, *OPTIONS)
	xpr_display_options.pack()
	
	xpr_seq_var=tk.StringVar()
	xpr_seq_label=tk.Label(window, text='Sequence Order')
	xpr_seq_label.pack()
	xpr_seq_entry=tk.Entry(window, textvariable=xpr_seq_var)
	xpr_seq_entry.pack()

	xpr_loop_lab=tk.Label(window, text='Loop Duration')
	xpr_loop_lab.pack()
	xpr_loop_var=tk.StringVar()
	xpr_loop_var.set('l')
	play_once=tk.Radiobutton(window, text='Play Once', variable=xpr_loop_var, value=20, command=loopdur)
	play_once.pack()
	play_loop=tk.Radiobutton(window, text='Loop', variable=xpr_loop_var, value=21, command=loopdur)
	play_loop.pack()

def loopdur():
	global loopduration, trans_off_label, manual, auto, trans_var, num_frames_var, num_frames_lab, num_frames_entry
	play_once.config(state='disabled')
	play_loop.config(state='disabled')
	if(xpr_loop_var.get()=='20'):
		trans_off_label=tk.Label(window, text='Transition Off')
		trans_off_label.pack()
		trans_var=tk.StringVar()
		trans_var.set('l')
		manual=tk.Radiobutton(window, text='Manual', variable=trans_var, value=22, command=xpr_name)
		manual.pack()
		auto=tk.Radiobutton(window, text='Auto', variable=trans_var, value=22, command=xpr_name)
		auto.pack()
	if(xpr_loop_var.get()=='21'):
		num_frames_var=tk.StringVar()
		num_frames_lab=tk.Label(window, text='Number of Frames')
		num_frames_lab.pack()
		num_frames_entry=tk.Entry(window, textvariable=num_frames_var)
		num_frames_entry.pack()
		
		trans_off_label=tk.Label(window, text='Transition Off')
		trans_off_label.pack()
		trans_var=tk.StringVar()
		trans_var.set('l')
		manual=tk.Radiobutton(window, text='Manual', variable=trans_var, value=22, command=xpr_name)
		manual.pack()
		auto=tk.Radiobutton(window, text='Auto', variable=trans_var, value=23, command=xpr_name)
		auto.pack()

def xpr_name():
	global man_tran, num_secs_label, nums_secs_var, num_secs_entry, xpr_version_var, xpr_version_entry, xpr_version_label, xpr_submit_butt
	
	
	if(trans_var.get()=='22'):
		auto.config(state='disabled')
		manual.config(state='disabled')
		man_tran="M-off"
		xpr_version_label=tk.Label(window, text='Version')
		xpr_version_label.pack()
		xpr_version_var=tk.StringVar()
		xpr_version_entry=tk.Entry(window, textvariable=xpr_version_var)
		xpr_version_entry.pack()
		xpr_submit_butt=tk.Button(window, text='Submit', command=xpr_submit)
		xpr_submit_butt.pack()
	if(trans_var.get()=='23'):
		auto.config(state='disabled')
		manual.config(state='disabled')
		
		num_secs_label=tk.Label(window, text='Number of Seconds')
		num_secs_label.pack()
		nums_secs_var=tk.StringVar()
		num_secs_entry=tk.Entry(window, textvariable=nums_secs_var)
		num_secs_entry.pack()
		
		
		xpr_version_label=tk.Label(window, text='Version')
		xpr_version_label.pack()
		xpr_version_var=tk.StringVar()
		xpr_version_entry=tk.Entry(window, textvariable=xpr_version_var)
		xpr_version_entry.pack()
		
		
		xpr_submit_butt=tk.Button(window, text='Submit', command=xpr_submit)
		xpr_submit_butt.pack()
		
def xpr_submit():
	global copyed_to_clip, xpr_refresh_butt, xpr_quit_butt
	if(trans_var.get()=='22'):
		man_tran="M-off"
	if(trans_var.get()=='23'):
		man_tran='auto'+nums_secs_var.get()
	if(xpr_loop_var.get()=='21'):
		loopduration="Loop-"+num_frames_var.get()
	if(xpr_loop_var.get()=='20'):
		loopduration="PlayOnce"
	xpr_text=xpr_content_var.get()+'_'+xpr_display_var.get()+'_'+xpr_seq_var.get()+'_'+loopduration+'_'+man_tran+'_V'+xpr_version_var.get()
	
	window.clipboard_clear()
	window.clipboard_append(xpr_text)
	window.update()
	copyed_to_clip=tk.Label(window, text="File Name Copyed to the Clipboard")
	copyed_to_clip.pack()
	
	xpr_refresh_butt=tk.Button(window, text='Refresh', command=xpr_refresh)
	xpr_refresh_butt.pack()
	xpr_quit_butt=tk.Button(window, text='Quit', command=quit)
	xpr_quit_butt.pack()
	
	#print(xpr_text)
def xpr_refresh():
	copyed_to_clip.config(text='')
	xpr_version_entry.pack_forget()
	xpr_version_label.pack_forget()
	if(trans_var.get()=='23'):
		num_secs_entry.pack_forget()
		num_secs_label.pack_forget()
	if(xpr_loop_var.get()=='21'):
		num_frames_lab.pack_forget()
		num_frames_entry.pack_forget()
	auto.pack_forget()
	manual.pack_forget()
	trans_off_label.pack_forget()
	xpr_content_label.pack_forget()
	xpr_content_entry.pack_forget()
	xpr_display_label.pack_forget()
	xpr_display_options.pack_forget()
	xpr_seq_label.pack_forget()
	xpr_seq_entry.pack_forget()
	xpr_loop_lab.pack_forget()
	play_once.pack_forget()
	play_loop.pack_forget()
	xpr_refresh_butt.pack_forget()
	cross_butt.config(state='active')
	cross_butt.deselect()
	xpr_butt.config(state='active')
	xpr_butt.deselect()
	rep_butt.config(state='active')
	rep_butt.deselect()
	dak_butt.config(state='active')
	dak_butt.deselect()
	v.set('L')
	xpr_quit_butt.pack_forget()
	xpr_submit_butt.pack_forget()
	
window=tk.Tk()
window.title("File Name Pro")
window.geometry("600x800")	
lbl=tk.Label(window, text="Choose System: ")
lbl.pack()		

v=tk.StringVar()
v.set("L")

cross_butt=tk.Radiobutton(window, text="Crossfire",  value=1, variable=v,command=callback1)
cross_butt.pack(anchor=tk.W)
xpr_butt=tk.Radiobutton(window, text="Xpression", value=2,variable=v, command=callback2)
xpr_butt.pack(anchor=tk.W)
rep_butt=tk.Radiobutton(window, text="Replay", value=3,variable=v, command=callback3)
rep_butt.pack(anchor=tk.W)
dak_butt=tk.Radiobutton(window, text="Dak", value=4,variable=v, command=dak_callback)
dak_butt.pack(anchor=tk.W)
window.mainloop()