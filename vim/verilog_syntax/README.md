# sv/uvm syntax enable, may need some change
* copy verilog_systemverilog.vom to vim install dir: /usr/share/vim/vim80/syntax
* update filetype.vim in dir. /usr/share/vim/vim80
```
 " Verilog-AMS HDL
 " au BufNewFile,BufRead *.va,*.vams     setf verilogams

 " SystemVerilog
 au BufNewFile,BufRead *.sv,*.svh,*.v        setf verilog_systemverilog
```
