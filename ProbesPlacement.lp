\* Probes_Placement_Problem *\
Minimize
Sum_of_Measurement_Costs: 2 Route_A_AB + 2 Route_A_AF + 3 Route_B_AB
 + 3 Route_B_BC + 3 Route_B_BF + 4 Route_C_BC + 4 Route_C_CD + 4 Route_C_CE
 + 4 Route_C_CF + 2 Route_D_CD + 2 Route_D_DE + 3 Route_E_CE + 3 Route_E_DE
 + 3 Route_E_EF + 4 Route_F_AF + 4 Route_F_BF + 4 Route_F_CF + 4 Route_F_EF
Subject To
Sum_of_Probes_out_of_route_A: Route_A_AB + Route_A_AF <= 2
Sum_of_Probes_out_of_route_B: Route_B_AB + Route_B_BC + Route_B_BF <= 3
Sum_of_Probes_out_of_route_C: Route_C_BC + Route_C_CD + Route_C_CE
 + Route_C_CF <= 4
Sum_of_Probes_out_of_route_D: Route_D_CD + Route_D_DE <= 2
Sum_of_Probes_out_of_route_E: Route_E_CE + Route_E_DE + Route_E_EF <= 3
Sum_of_Probes_out_of_route_F: Route_F_AF + Route_F_BF + Route_F_CF
 + Route_F_EF <= 4
Sum_of_Products_into_LinkAB: Route_A_AB + Route_B_AB = 1
Sum_of_Products_into_LinkAF: Route_A_AF + Route_F_AF = 1
Sum_of_Products_into_LinkBC: Route_B_BC + Route_C_BC = 1
Sum_of_Products_into_LinkBF: Route_B_BF + Route_F_BF = 1
Sum_of_Products_into_LinkCD: Route_C_CD + Route_D_CD = 1
Sum_of_Products_into_LinkCE: Route_C_CE + Route_E_CE = 1
Sum_of_Products_into_LinkCF: Route_C_CF + Route_F_CF = 1
Sum_of_Products_into_LinkDE: Route_D_DE + Route_E_DE = 1
Sum_of_Products_into_LinkEF: Route_E_EF + Route_F_EF = 1
Bounds
 0 <= Route_A_AB
 0 <= Route_A_AF
 0 <= Route_B_AB
 0 <= Route_B_BC
 0 <= Route_B_BF
 0 <= Route_C_BC
 0 <= Route_C_CD
 0 <= Route_C_CE
 0 <= Route_C_CF
 0 <= Route_D_CD
 0 <= Route_D_DE
 0 <= Route_E_CE
 0 <= Route_E_DE
 0 <= Route_E_EF
 0 <= Route_F_AF
 0 <= Route_F_BF
 0 <= Route_F_CF
 0 <= Route_F_EF
Generals
Route_A_AB
Route_A_AF
Route_B_AB
Route_B_BC
Route_B_BF
Route_C_BC
Route_C_CD
Route_C_CE
Route_C_CF
Route_D_CD
Route_D_DE
Route_E_CE
Route_E_DE
Route_E_EF
Route_F_AF
Route_F_BF
Route_F_CF
Route_F_EF
End
