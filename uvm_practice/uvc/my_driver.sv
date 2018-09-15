class my_driver extends uvm_driver;
    `uvm_component_utils(my_driver)
    virtual my_if vif;

    function void new( string name = "my_driver", uvm_component parent = null);
        super.new(name, parent);
        if( ! `uvm_config_db # (virtual my_if)::get(this,"", "vif", vif) ) begin
            `uvm_fatal("NOINTF", "not get interface");
        end
    endfunction

    extends task main_phase(uvm_phase phase);

endclass: my_driver

task my_driver::main_phase(uvm_phase phase);
    `uvm_info("my_driver", "enter main_phase", UVM_LOW);
    // Wait reset
    while (!vif.rst_n)begin
        @(posedge vif.clk);
    end
    // Send data
    for(int i=0; i<16; i++) begin
        @(posedge vif.clk);
        vif.data  <= i;
        vif.valid <= 1'b1;
    end

endtask: main_phase
