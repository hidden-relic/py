import tkinter as tk
from tkinter import ttk
from turtle import RawTurtle


class Framing:
    def __init__(self):


            self.x = 0
            self.y = 0
            self.myfont = ('Verdana', 10)
            self.infofont = ('Verdana', 8)
            self.root = tk.Tk()


            self.vals =
            for i in range(0, 500):
                self.vals['ft'].append(i)
                if i < 12:
                    self.vals['in'].append(i)
                    self.buildNotebooks()
                    self.buildRoofInput()
                    self.buildRoofData()
                    self.buildRoofDraw()
                    self.buildDeckInput()
                    self.buildDeckData()
                    self.buildDeckDraw()


                    def buildNotebooks(self):


                        def mainNotebook(self):


                            self.main_notebook = ttk.Notebook(self.root)
                            self.main_notebook.pack(fill='both')
                            self.roof_tab = tk.Frame(self.main_notebook)
                            self.roof_tab.pack()
                            self.main_notebook.add(self.roof_tab, text='Roof')
                            self.deck_tab = tk.Frame(self.main_notebook)
                            self.deck_tab.pack()
                            self.main_notebook.add(self.deck_tab, text='Deck')


                            def subNotebook(self):


                                def subRoofTab(self):
                                        self.sub_notebook_roof = ttk.Notebook(self.roof_tab)
                                            self.sub_notebook_roof.pack(fill='both')
                                                self.roof_input_tab = tk.Frame(self.sub_notebook_roof)
                                                    self.roof_input_tab.pack()
                                                        self.sub_notebook_roof.add(self.roof_input_tab, text='Input')
                                                            self.roof_data_tab = tk.Frame(self.sub_notebook_roof)
                                                                self.roof_data_tab.pack()
                                                                    self.sub_notebook_roof.add(self.roof_data_tab, text='Data')
                                                                        self.roof_draw_tab = tk.Frame(self.sub_notebook_roof)
                                                                            self.roof_draw_tab.pack(fill='both')
                                                                                self.sub_notebook_roof.add(self.roof_draw_tab, text='Draw')


                                                                                def subDeckTab(self):
                                                                                        self.sub_notebook_deck = ttk.Notebook(self.deck_tab)
                                                                                            self.sub_notebook_deck.pack(fill='both')
                                                                                                self.deck_input_tab = tk.Frame(self.sub_notebook_deck)
                                                                                                    self.deck_input_tab.pack()
                                                                                                        self.sub_notebook_deck.add(self.deck_input_tab, text='Input')
                                                                                                            self.deck_data_tab = tk.Frame(self.sub_notebook_deck)
                                                                                                                self.deck_data_tab.pack()
                                                                                                                    self.sub_notebook_deck.add(self.deck_data_tab, text='Data')
                                                                                                                        self.deck_draw_tab = tk.Frame(self.sub_notebook_deck)
                                                                                                                            self.deck_draw_tab.pack()
                                                                                                                                self.sub_notebook_deck.add(self.deck_draw_tab, text='Draw')


                                                                                                                                subRoofTab(self)
                                                                                                                                subDeckTab(self)
                                                                                                                                mainNotebook(self)
                                                                                                                                subNotebook(self)



                                                                                                                                def buildRoofInput(self):


                                                                                                                                    self.roof_width_input_frame = tk.Frame(self.roof_input_tab)
                                                                                                                                    self.roof_width_input_frame.pack()
                                                                                                                                    self.roof_depth_input_frame = tk.Frame(self.roof_input_tab)
                                                                                                                                    self.roof_depth_input_frame.pack()

                                                                                                                                    self.roof_width_lbl_frame = tk.Frame(self.roof_width_input_frame)
                                                                                                                                    tk.Label(self.roof_width_lbl_frame, text="Building width:",
                                                                                                                                                      font=self.myfont).pack(side='top', padx=12, pady=1)
                                                                                                                                    self.roof_width_lbl_frame.pack(side='top')

                                                                                                                                    self.roof_depth_lbl_frame = tk.Frame(self.roof_depth_input_frame)
                                                                                                                                    tk.Label(self.roof_depth_lbl_frame, text="Building depth:",
                                                                                                                                                      font=self.myfont).pack(side='top', padx=12, pady=1)
                                                                                                                                    self.roof_depth_lbl_frame.pack(side='top')


                                                                                                                                    def buildWidth(self):


                                                                                                                                        self.roof_width_measurements_frame = tk.Frame(self.roof_width_input_frame)


                                                                                                                                        def buildWFt(self):


                                                                                                                                            self.roof_width_ft_frame = tk.Frame(self.roof_width_measurements_frame)
                                                                                                                                            self.roof_width_ft_frame.grid(column=0, row=0, sticky='w')
                                                                                                                                            tk.Label(self.roof_width_ft_frame, text="ft.",
                                                                                                                                                              font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                            self.roof_width_ft = ttk.Combobox(self.roof_width_ft_frame, height=20, width=6, values=tuple(
                                                                                                                                                    self.vals['ft']), font=self.myfont, state='readonly')
                                                                                                                                            self.roof_width_ft.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                            self.roof_width_ft.set(10)


                                                                                                                                            def buildWIn(self):


                                                                                                                                                self.roof_width_in_frame = tk.Frame(self.roof_width_measurements_frame)
                                                                                                                                                self.roof_width_in_frame.grid(column=1, row=0)
                                                                                                                                                tk.Label(self.roof_width_in_frame, text="in.",
                                                                                                                                                                  font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                self.roof_width_in = ttk.Combobox(self.roof_width_in_frame, height=20, width=6, values=tuple(
                                                                                                                                                        self.vals['in']), font=self.myfont, state='readonly')
                                                                                                                                                self.roof_width_in.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                self.roof_width_in.set(0)


                                                                                                                                                def buildWFr(self):


                                                                                                                                                    self.roof_width_fr_frame = tk.Frame(self.roof_width_measurements_frame)
                                                                                                                                                    self.roof_width_fr_frame.grid(column=2, row=0, sticky='e')
                                                                                                                                                    tk.Label(self.roof_width_fr_frame, text=bytes.fromhex(
                                                                                                                                                            'BE'), font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                    self.roof_width_fr = ttk.Combobox(self.roof_width_fr_frame, height=20, width=6, values=(
                                                                                                                                                            "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state='readonly')
                                                                                                                                                    self.roof_width_fr.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                    self.roof_width_fr.set(0)
                                                                                                                                                    buildWFt(self)
                                                                                                                                                    buildWIn(self)
                                                                                                                                                    buildWFr(self)

                                                                                                                                                    self.roof_width_measurements_frame.pack(side='top')
                                                                                                                                                    self.roof_width_input_frame.pack(fill='x')
                                                                                                                                                    ttk.Separator(self.roof_width_input_frame,
                                                                                                                                                                                orient='horizontal').pack(fill='both', pady=12)


                                                                                                                                                    def buildDepth(self):


                                                                                                                                                        self.roof_depth_measurements_frame = tk.Frame(
                                                                                                                                                                self.roof_depth_input_frame)


                                                                                                                                                        def buildDFt(self):


                                                                                                                                                            self.roof_depth_ft_frame = tk.Frame(self.roof_depth_measurements_frame)
                                                                                                                                                            self.roof_depth_ft_frame.grid(column=0, row=0, sticky='w')
                                                                                                                                                            tk.Label(self.roof_depth_ft_frame, text="ft.",
                                                                                                                                                                              font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                            self.roof_depth_ft = ttk.Combobox(self.roof_depth_ft_frame, height=20, width=6, values=tuple(
                                                                                                                                                                    self.vals['ft']), font=self.myfont, state='readonly')
                                                                                                                                                            self.roof_depth_ft.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                            self.roof_depth_ft.set(10)


                                                                                                                                                            def buildDIn(self):


                                                                                                                                                                self.roof_depth_in_frame = tk.Frame(self.roof_depth_measurements_frame)
                                                                                                                                                                self.roof_depth_in_frame.grid(column=1, row=0)
                                                                                                                                                                tk.Label(self.roof_depth_in_frame, text="in.",
                                                                                                                                                                                  font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                self.roof_depth_in = ttk.Combobox(self.roof_depth_in_frame, height=20, width=6, values=tuple(
                                                                                                                                                                        self.vals['in']), font=self.myfont, state='readonly')
                                                                                                                                                                self.roof_depth_in.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                self.roof_depth_in.set(0)


                                                                                                                                                                def buildDFr(self):


                                                                                                                                                                    self.roof_depth_fr_frame = tk.Frame(self.roof_depth_measurements_frame)
                                                                                                                                                                    self.roof_depth_fr_frame.grid(column=2, row=0, sticky='e')
                                                                                                                                                                    tk.Label(self.roof_depth_fr_frame, text=bytes.fromhex(
                                                                                                                                                                            'BE'), font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                    self.roof_depth_fr = ttk.Combobox(self.roof_depth_fr_frame, height=20, width=6, values=(
                                                                                                                                                                            "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state='readonly')
                                                                                                                                                                    self.roof_depth_fr.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                    self.roof_depth_fr.set(0)

                                                                                                                                                                    buildDFt(self)
                                                                                                                                                                    buildDIn(self)
                                                                                                                                                                    buildDFr(self)

                                                                                                                                                                    self.roof_depth_measurements_frame.pack(side='top')
                                                                                                                                                                    self.roof_depth_input_frame.pack(fill='x')
                                                                                                                                                                    ttk.Separator(self.roof_depth_input_frame,
                                                                                                                                                                                                orient='horizontal').pack(fill='both', pady=12)


                                                                                                                                                                    def buildOther(self):


                                                                                                                                                                        self.roof_other_frame = tk.Frame(self.roof_input_tab)
                                                                                                                                                                        self.roof_pitch_lbl = tk.Label(
                                                                                                                                                                                self.roof_other_frame, text='Pitch: ', font=self.myfont)
                                                                                                                                                                        self.roof_pitch_lbl.pack(side='left', padx=12, pady=12)
                                                                                                                                                                        self.roof_pitch = tk.Entry(
                                                                                                                                                                                self.roof_other_frame, width=4, font=self.myfont, justify='center')
                                                                                                                                                                        self.roof_pitch.pack(side='left', padx=12, pady=12)
                                                                                                                                                                        self.roof_pitch.insert(0, 9)

                                                                                                                                                                        self.roof_tail = tk.Entry(self.roof_other_frame,
                                                                                                                                                                                                                            width=4, font=self.myfont, justify='center')
                                                                                                                                                                        self.roof_tail.pack(side='right', padx=12, pady=12)
                                                                                                                                                                        self.roof_tail.insert(0, 12)
                                                                                                                                                                        self.roof_tail_lbl = tk.Label(
                                                                                                                                                                                self.roof_other_frame, text='Soffit: ', font=self.myfont)
                                                                                                                                                                        self.roof_tail_lbl.pack(side='right', padx=12, pady=12)

                                                                                                                                                                        self.roof_other_frame.pack(fill='x', padx=12)
                                                                                                                                                                        self.roof_go_btn = tk.Button(
                                                                                                                                                                                self.roof_input_tab, text="GO", command=self.roofClicked)
                                                                                                                                                                        self.roof_go_btn.pack()
                                                                                                                                                                        buildWidth(self)
                                                                                                                                                                        buildDepth(self)
                                                                                                                                                                        buildOther(self)


                                                                                                                                                                        def buildRoofData(self):


                                                                                                                                                                            pass


                                                                                                                                                                        def buildRoofDraw(self):


                                                                                                                                                                            self.roof_draw_frame = tk.Frame(self.roof_draw_tab)
                                                                                                                                                                            self.roof_draw_frame.pack(fill='both', expand=True)
                                                                                                                                                                            self.roof_canvas = tk.Canvas(self.roof_draw_frame, width=1.0, height=0.5)
                                                                                                                                                                            self.roof_canvas.pack(fill='both', expand=True)
                                                                                                                                                                            self.t = RawTurtle(self.roof_canvas)
                                                                                                                                                                            self.screen = self.t.getscreen()
                                                                                                                                                                            self.screen.reset()
                                                                                                                                                                            self.t.reset()


                                                                                                                                                                            def roofClicked(self):


                                                                                                                                                                                pass



                                                                                                                                                                            def buildDeckInput(self):


                                                                                                                                                                                self.deck_width_input_frame = tk.Frame(self.deck_input_tab)
                                                                                                                                                                                self.deck_width_input_frame.pack()
                                                                                                                                                                                self.deck_length_input_frame = tk.Frame(self.deck_input_tab)
                                                                                                                                                                                self.deck_length_input_frame.pack()
                                                                                                                                                                                self.deck_material_width_frame = tk.Frame(self.deck_input_table)
                                                                                                                                                                                self.deck_material_width_frame.pack()

                                                                                                                                                                                self.deck_width_lbl_frame = tk.Frame(self.deck_width_input_frame)
                                                                                                                                                                                tk.Label(self.deck_width_lbl_frame, text="Building width:",
                                                                                                                                                                                                  font=self.myfont).pack(side='top', padx=12, pady=1)
                                                                                                                                                                                self.deck_width_lbl_frame.pack(side='top')

                                                                                                                                                                                self.deck_length_lbl_frame = tk.Frame(self.deck_length_input_frame)
                                                                                                                                                                                tk.Label(self.deck_length_lbl_frame, text="Building length:",
                                                                                                                                                                                                  font=self.myfont).pack(side='top', padx=12, pady=1)
                                                                                                                                                                                self.deck_length_lbl_frame.pack(side='top')


                                                                                                                                                                                def buildWidth(self):


                                                                                                                                                                                    self.deck_width_measurements_frame = tk.Frame(self.deck_width_input_frame)


                                                                                                                                                                                    def buildWFt(self):


                                                                                                                                                                                        self.deck_width_ft_frame = tk.Frame(self.deck_width_measurements_frame)
                                                                                                                                                                                        self.deck_width_ft_frame.grid(column=0, row=0, sticky='w')
                                                                                                                                                                                        tk.Label(self.deck_width_ft_frame, text="ft.",
                                                                                                                                                                                                          font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                        self.deck_width_ft = ttk.Combobox(self.deck_width_ft_frame, height=20, width=6, values=tuple(
                                                                                                                                                                                                self.vals['ft']), font=self.myfont, state='readonly')
                                                                                                                                                                                        self.deck_width_ft.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                        self.deck_width_ft.set(10)


                                                                                                                                                                                        def buildWIn(self):


                                                                                                                                                                                            self.deck_width_in_frame = tk.Frame(self.deck_width_measurements_frame)
                                                                                                                                                                                            self.deck_width_in_frame.grid(column=1, row=0)
                                                                                                                                                                                            tk.Label(self.deck_width_in_frame, text="in.",
                                                                                                                                                                                                              font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                            self.deck_width_in = ttk.Combobox(self.deck_width_in_frame, height=20, width=6, values=tuple(
                                                                                                                                                                                                    self.vals['in']), font=self.myfont, state='readonly')
                                                                                                                                                                                            self.deck_width_in.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                            self.deck_width_in.set(0)


                                                                                                                                                                                            def buildWFr(self):


                                                                                                                                                                                                self.deck_width_fr_frame = tk.Frame(self.deck_width_measurements_frame)
                                                                                                                                                                                                self.deck_width_fr_frame.grid(column=2, row=0, sticky='e')
                                                                                                                                                                                                tk.Label(self.deck_width_fr_frame, text=bytes.fromhex(
                                                                                                                                                                                                        'BE'), font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                self.deck_width_fr = ttk.Combobox(self.deck_width_fr_frame, height=20, width=6, values=(
                                                                                                                                                                                                        "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state='readonly')
                                                                                                                                                                                                self.deck_width_fr.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                self.deck_width_fr.set(0)
                                                                                                                                                                                                buildWFt(self)
                                                                                                                                                                                                buildWIn(self)
                                                                                                                                                                                                buildWFr(self)

                                                                                                                                                                                                self.deck_width_measurements_frame.pack(side='top')
                                                                                                                                                                                                self.deck_width_input_frame.pack(fill='x')
                                                                                                                                                                                                ttk.Separator(self.deck_width_input_frame,
                                                                                                                                                                                                                            orient='horizontal').pack(fill='both', pady=12)


                                                                                                                                                                                                def buildLength(self):


                                                                                                                                                                                                    self.deck_length_measurements_frame = tk.Frame(self.deck_length_input_frame)


                                                                                                                                                                                                    def buildDFt(self):


                                                                                                                                                                                                        self.deck_length_ft_frame = tk.Frame(self.deck_length_measurements_frame)
                                                                                                                                                                                                        self.deck_length_ft_frame.grid(column=0, row=0, sticky='w')
                                                                                                                                                                                                        tk.Label(self.deck_length_ft_frame, text="ft.", font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                        self.deck_length_ft = ttk.Combobox(self.deck_length_ft_frame, height=20, width=6,
                                                                                                                                                                                                                                                                              values=tuple(self.vals['ft']), font=self.myfont, state='readonly')
                                                                                                                                                                                                        self.deck_length_ft.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                        self.deck_length_ft.set(10)


                                                                                                                                                                                                        def buildDIn(self):


                                                                                                                                                                                                            self.deck_length_in_frame = tk.Frame(
                                                                                                                                                                                                                    self.deck_length_measurements_frame)
                                                                                                                                                                                                            self.deck_length_in_frame.grid(column=1, row=0)
                                                                                                                                                                                                            tk.Label(self.deck_length_in_frame, text="in.",
                                                                                                                                                                                                                              font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                            self.deck_length_in = ttk.Combobox(self.deck_length_in_frame, height=20, width=6, values=tuple(
                                                                                                                                                                                                                    self.vals['in']), font=self.myfont, state='readonly')
                                                                                                                                                                                                            self.deck_length_in.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                            self.deck_length_in.set(0)


                                                                                                                                                                                                            def buildDFr(self):


                                                                                                                                                                                                                self.deck_length_fr_frame = tk.Frame(
                                                                                                                                                                                                                        self.deck_length_measurements_frame)
                                                                                                                                                                                                                self.deck_length_fr_frame.grid(column=2, row=0, sticky='e')
                                                                                                                                                                                                                tk.Label(self.deck_length_fr_frame, text=bytes.fromhex(
                                                                                                                                                                                                                        'BE'), font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                                self.deck_length_fr = ttk.Combobox(self.deck_length_fr_frame, height=20, width=6, values=(
                                                                                                                                                                                                                        "0", "1/16", "1/8", "3/16", "1/4", "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state='readonly')
                                                                                                                                                                                                                self.deck_length_fr.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                                self.deck_length_fr.set(0)

                                                                                                                                                                                                                buildDFt(self)
                                                                                                                                                                                                                buildDIn(self)
                                                                                                                                                                                                                buildDFr(self)

                                                                                                                                                                                                                self.deck_length_measurements_frame.pack(side='top')
                                                                                                                                                                                                                self.deck_length_input_frame.pack(fill='x')
                                                                                                                                                                                                                ttk.Separator(self.deck_length_input_frame,
                                                                                                                                                                                                                                            orient='horizontal').pack(fill='both', pady=12)


                                                                                                                                                                                                                def buildOther(self):


                                                                                                                                                                                                                    self.deck_other_frame = tk.Frame(self.deck_input_tab)


                                                                                                                                                                                                                    def buildDIn(self):


                                                                                                                                                                                                                        self.deck_length_in_frame = tk.Frame(
                                                                                                                                                                                                                                self.deck_length_measurements_frame)
                                                                                                                                                                                                                        self.deck_length_in_frame.grid(column=1, row=0)
                                                                                                                                                                                                                        tk.Label(self.deck_length_in_frame, text="in.",
                                                                                                                                                                                                                                          font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                                        self.deck_length_in = ttk.Combobox(self.deck_length_in_frame, height=20, width=6, values=tuple(
                                                                                                                                                                                                                                self.vals['in']), font=self.myfont, state='readonly')
                                                                                                                                                                                                                        self.deck_length_in.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                                        self.deck_length_in.set(0)
                                                                                                                                                                                                                        def buildDFr(self):


                                                                                                                                                                                                                            self.deck_length_fr_frame = tk.Frame(self.deck_length_measurements_frame)
                                                                                                                                                                                                                            self.deck_length_fr_frame.grid(column=2, row=0, sticky='e')
                                                                                                                                                                                                                            tk.Label(self.deck_length_fr_frame, text=bytes.fromhex('BE'), font=self.myfont).pack(padx=6, ipadx=12)
                                                                                                                                                                                                                            self.deck_length_fr = ttk.Combobox(self.deck_length_fr_frame, height=20, width=6, values=("0", "1/16", "1/8", "3/16", "1/4",
                                                                                                                                                                                                                                                                                                                                                         "5/16", "3/8", "7/16", "1/2", "9/16", "5/8", "11/16", "3/4", "13/16", "7/8", "15/16"), font=self.myfont, state='readonly')
                                                                                                                                                                                                                            self.deck_length_fr.pack(padx=6, pady=12, ipadx=12)
                                                                                                                                                                                                                            self.deck_length_fr.set(0)
                                                                                                                                                                                                                            self.deck_pitch_lbl = tk.Label(self.deck_other_frame, text='Pitch: ', font=self.myfont)
                                                                                                                                                                                                                            self.deck_pitch_lbl.pack(side='left', padx=12, pady=12)
                                                                                                                                                                                                                            self.deck_pitch = tk.Entry(self.deck_other_frame, width=4, font=self.myfont, justify='center')
                                                                                                                                                                                                                            self.deck_pitch.pack(side='left', padx=12, pady=12)
                                                                                                                                                                                                                            self.deck_pitch.insert(0, 9)

                                                                                                                                                                                                                            self.deck_tail = tk.Entry(self.deck_other_frame, width=4, font=self.myfont, justify='center')
                                                                                                                                                                                                                            self.deck_tail.pack(side='right', padx=12, pady=12)
                                                                                                                                                                                                                            self.deck_tail.insert(0, 12)
                                                                                                                                                                                                                            self.deck_tail_lbl = tk.Label(self.deck_other_frame, text='Soffit: ', font=self.myfont)
                                                                                                                                                                                                                            self.deck_tail_lbl.pack(side='right', padx=12, pady=12)

                                                                                                                                                                                                                            self.deck_other_frame.pack(fill='x', padx=12)
                                                                                                                                                                                                                            self.deck_go_btn = tk.Button(self.deck_input_tab, text="GO", command=self.deckClicked)
                                                                                                                                                                                                                            self.deck_go_btn.pack()
                                                                                                                                                                                                                            buildWidth(self)
                                                                                                                                                                                                                            buildLength(self)
                                                                                                                                                                                                                            buildOther(self)


                                                                                                                                                                                                                            def buildDeckData(self):


                                                                                                                                                                                                                                pass


                                                                                                                                                                                                                            def buildDeckDraw(self):


                                                                                                                                                                                                                                self.deck_draw_frame = tk.Frame(self.deck_draw_tab)
                                                                                                                                                                                                                                self.deck_draw_frame.pack(fill='both', expand=True)
                                                                                                                                                                                                                                self.deck_canvas = tk.Canvas(self.deck_draw_frame, width=1.0, height=0.5)
                                                                                                                                                                                                                                self.deck_canvas.pack(fill='both', expand=True)
                                                                                                                                                                                                                                self.t = RawTurtle(self.deck_canvas)
                                                                                                                                                                                                                                self.screen = self.t.getscreen()
                                                                                                                                                                                                                                self.screen.reset()
                                                                                                                                                                                                                                self.t.reset()


                                                                                                                                                                                                                                def deckClicked(self):


                                                                                                                                                                                                                                    pass
                                                                                                                                                                                                                                def onClick(self, x, y):


                                                                                                                                                                                                                                    self.x + 3
                                                                                                                                                                                                                                    self.y -= 3
                                                                                                                                                                                                                                    self.t.goto(self.x, self.y)
                                                                                                                                                                                                                                    for i in range(0, 4):
                                                                                                                                                                                                                                        self.t.stamp()
                                                                                                                                                                                                                                        self.t.right(90)
                                                                                                                                                                                                                                        self.t.write(str(self.x)" 'Str(self.y), align='left', font=('Verdana', 6))

                                                                                                                                                                                                                                                     f = Framing()
                                                                                                                                                                                                                                                     f.screen.onclick(f.onClick)
                                                                                                                                                                                                                                                     f.root.mainloop()
                                                                                                                                                                                                                                                     