
height_pd1=12;
 height_pd=12;
   color("grey")
   
 difference(){
 union() {
   

    
      translate([0,3.5,11]) 
    
     cube ([43.5,20,22], center=true);  //bottom 
       translate([0,20,11]) 
     
       cube ([43.5,15,22], center=true);
 }
 union() {
        translate([2,5.8,11])
     
          cube ([41.0,14,14], center=true); 
        translate([0,20,28]) 
    
           cube ([41.0,12.5,55], center=true); 
        translate([0,12,height_pd1]) 
    
           cube([16,5,8], center=true);//optical sensor window
        translate([-5,28,height_pd1]) 
     
           cube([24,5,16], center=true);//oled screen
     
           translate([2,-4,11]) 
   
     cube ([46,3,15], center=true);  //optical_filter
     
        translate([0,0,height_pd1]) 
   
           cube([36,8,8], center=true);//optical sensor window 
 
 
     
 }
 }



