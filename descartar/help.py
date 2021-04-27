#num = int(1000)

#for i in range(0,10):
#    print('{}{}'.format(num, i))

#for i in range(num):
#    print(i)

#for i in range(0,320):
#    print(i)

exame = str(" insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem,paciente_cpf,  paciente_idpaciente) values(?, ?, ?, ?, ?, ?, ?,?, ?);")

paciente = str("insert into paciente (cpf, nome) values (?,?);")

#for i in range(1,321):
#     print('insert into paciente (cpf, nome) values ({}, "paciente{}");'.format(1000 + i, i ))

id = int(67)

for i in range(1,321):
    print('insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem,paciente_cpf,  paciente_idpaciente) values(?, ?, ?, ?, ?, ?, ?,?, ?);')

#select *from paciente;
#select *from exame;
#delete from exame where  idexame = 30;  

1st column: MIAS database reference number.

2nd column: Character of background tissue: 
                F - Fatty 
                G - Fatty-glandular
                D - Dense-glandular

3rd column: Class of abnormality present:
                CALC - Calcification
                CIRC - Well-defined/circumscribed masses
                SPIC - Spiculated masses
                MISC - Other, ill-defined masses
                ARCH - Architectural distortion
                ASYM - Asymmetry
                NORM - Normal

4th column: Severity of abnormality;
                B - Benign
                M - Malignant
                
5th,6th columns: x,y image-coordinates of centre of abnormality.

7th column: Approximate radius (in pixels) of a circle enclosing
	    the abnormality.


#----------------------------------------------------        
insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 535, 425, 197, "mdb001.PNG", 1001, 67);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 522, 280, 69, "mdb002.PNG", 1002, 68);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb003.PNG", 1003, 69);

#**************************************
   
#insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb004.PNG", 1004, 70);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 477, 133, 30, "mdb005.PNG", 1005, 71);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 500, 168, 26, "mdb005(2).PNG", 1005, 71);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM ", null, null, null, null, "mdb006.PNG", 1006, 72);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb007.PNG", 1007, 73);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb008.PNG", 1008, 74);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM ", null, null, null, null, "mdb009.PNG", 1009, 75);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 525, 425, 33, "mdb010.PNG", 1010, 76);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM ", null, null, null, null, "mdb011.PNG", 1011, 77);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 471, 458, 40, "mdb012.PNG", 1012, 78);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "MISC", "B", 667, 365, 31, "mdb013.PNG", 1013, 79);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb014.PNG", 1014, 80);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 595, 864, 68, "mdb015.PNG", 1015, 81);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb016.PNG", 1016, 82);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 547, 573, 48, "mdb017.PNG", 1017, 83);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb018.PNG", 1018, 84);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 653, 477, 49, "mdb019.PNG", 1019, 85);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb020.PNG", 1020, 86);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "B", 493, 125, 49, "mdb021.PNG", 1021, 87);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb022.PNG", 1022, 88);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "M", 538, 681, 29, "mdb023.PNG", 1023, 89);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb024.PNG", 1024, 90);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 674, 443, 79, "mdb025.PNG", 1025, 91);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM ", null, null, null, null, "mdb026.PNG", 1026, 92);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM ", null, null, null, null, "mdb027.PNG", 1027, 93);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "M", 338, 314, 56, "mdb028.PNG", 1028, 94);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb029.PNG", 1029, 95);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "MISC", "B", 322, 676, 43, "mdb030.PNG", 1030, 96);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM ", null, null, null, null, "mdb031.PNG", 1031, 97);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "MISC", "B", 388, 742, 66, "mdb032.PNG", 1032, 98);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb033.PNG", 1033, 99);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb034.PNG", 1034, 100);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb035.PNG", 1035, 101);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb036.PNG", 1036, 102);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb037.PNG", 1037, 103);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb038.PNG", 1038, 104);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb039.PNG", 1039, 105);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb040.PNG", 1040, 106);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb041.PNG", 1041, 107);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb042.PNG", 1042, 108);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb043.PNG", 1043, 109);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb044.PNG", 1044, 110);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb045.PNG", 1045, 111);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb046.PNG", 1046, 112);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb047.PNG", 1047, 113);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb048.PNG", 1048, 114);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb049.PNG", 1049, 115);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb050.PNG", 1050, 116);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb051.PNG", 1051, 117);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb052.PNG", 1052, 118);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb053.PNG", 1053, 119);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb054.PNG", 1054, 120);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb055.PNG", 1055, 121);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb056.PNG", 1056, 122);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb057.PNG", 1057, 123);

nsert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "MISC", "M", 318, 359, 27, "mdb058.PNG", 1058, 124);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", null, null, null, "mdb059.PNG", 1059, 125);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb060.PNG", 1060, 126);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb061.PNG", 1061, 127);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb062.PNG", 1062, 128);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "MISC", "B", 546, 463, 33, "mdb063.PNG", 1063, 129);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb064.PNG", 1064, 130);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb065.PNG", 1065, 131);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM ", null, null, null, null, "mdb066.PNG", 1066, 132);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb067.PNG", 1067, 133);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb068.PNG", 1068, 134);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 462, 406, 44, "mdb069.PNG", 1069, 135);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb070.PNG", 1070, 136);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb071.PNG", 1071, 137);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ASYM ", "M", 266, 517, 28, "mdb072.PNG", 1072, 138);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb073.PNG", 1073, 139);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb074.PNG", 1074, 140);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ASYM ", "M", 468, 717, 23, "mdb075.PNG", 1075, 141);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb076.PNG", 1076, 142);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb077.PNG", 1077, 143);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb078.PNG", 1078, 144);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb079.PNG", 1079, 145);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 432, 149, 20, "mdb080.PNG", 1080, 146);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ASYM", "B", 492, 473, 131, "mdb081.PNG", 1081, 147);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb082.PNG", 1082, 148);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ASYM", "B", 544, 194, 38, "mdb083.PNG", 1083, 149);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb084.PNG", 1084, 150);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb085.PNG", 1085, 151);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb086.PNG", 1086, 152);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb087.PNG", 1087, 153);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb088.PNG", 1088, 154);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb089.PNG", 1089, 155);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ASYM", "M", 510, 547, 49, "mdb090.PNG", 1090, 156);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 680, 494, 20, "mdb091.PNG", 1091, 157);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ASYM", "M", 423, 662, 43, "mdb092.PNG", 1092, 158);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, 
y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb093.PNG", 1093, 159);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb094.PNG", 1094, 160);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ASYM", "M", 466, 517, 29, "mdb095.PNG", 1095, 161);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, 
y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb096.PNG", 1096, 162);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ASYM", "B", 612, 297, 34, "mdb097.PNG", 1097, 163);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, 
y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb098.PNG", 1098, 164);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "B", 714, 340, 23, "mdb099.PNG", 1099, 165);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb100.PNG", 1100, 166);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb101.PNG", 1101, 167);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "M", 415, 460, 38, "mdb102.PNG", 1102, 168);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb103.PNG", 1103, 169);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "B", 357, 365, 50, "mdb104.PNG", 1104, 170);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "M", 516, 279, 98, "mdb105.PNG", 1105, 171);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb106.PNG", 1106, 172);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "B", 600, 621, 111, "mdb107.PNG", 1107, 173);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb108.PNG", 1108, 174);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb109.PNG", 1109, 175);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "M", 190, 427, 51, "mdb110.PNG", 1110, 176);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ASYM", "M", 505, 575, 107, "mdb111.PNG", 1111, 177);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb112.PNG", 1112, 178);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb113.PNG", 1113, 179);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb114.PNG", 1114, 180);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "M", 461, 532, 117, "mdb115.PNG", 1115, 181);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb116.PNG", 1116, 182);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "M", 480, 576, 84, "mdb117.PNG", 1117, 183);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb118.PNG", 1118, 184);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb119.PNG", 1119, 185);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "M", 423, 262, 79, "mdb120.PNG", 1120, 186);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "B", 492, 434, 87, "mdb121.PNG", 1121, 187);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb122.PNG", 1122, 188);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb123.PNG", 1123, 189);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "M", 366, 620, 33, "mdb124.PNG", 1124, 190);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "M", 700, 552, 60, "mdb125.PNG", 1125, 191);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "B", 191, 549, 23, "mdb126.PNG", 1126, 192);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "ARCH", "B", 523, 551, 48, "mdb127.PNG", 1127, 193);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb128.PNG", 1128, 194);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb129.PNG", 1129, 195);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "M", 220, 552, 28, "mdb130.PNG", 1130, 196);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb131.PNG", 1131, 197);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 252, 788, 52, "mdb132.PNG", 1132, 198);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 335, 766, 18, "mdb132(2).PNG", 1132, 198);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb133.PNG", 1133, 199);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "M", 469, 728, 49, "mdb134.PNG", 1134, 200);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb135.PNG", 1135, 201);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb136.PNG", 1136, 202);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb137.PNG", 1137, 203);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb138.PNG", 1138, 204);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb139.PNG", 1139, 205);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb140.PNG", 1140, 206);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "M", 470, 759, 29, "mdb141.PNG", 1141, 207);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CIRC", "B", 347, 636, 26, "mdb142.PNG", 1142, 208);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb143.PNG", 1143, 209);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "B", 233, 994, 29, "mdb144.PNG", 1144, 210);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "M", 313, 540, 27, "mdb144(2).PNG", 1144, 210);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "B", 669, 543, 49, "mdb145.PNG", 1145, 211);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb146.PNG", 1146, 212);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb147.PNG", 1147, 213);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "SPIC", "M", 326, 607, 174, "mdb148.PNG", 1148, 214);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb149.PNG", 1149, 215);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "B", 351, 661, 62, "mdb150.PNG", 1150, 216);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb151.PNG", 1151, 217);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "B", 675, 486, 48, "mdb152.PNG", 1152, 218);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb153.PNG", 1153, 219);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb154.PNG", 1154, 220);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "M", 448, 480, 95, "mdb155.PNG", 1155, 221);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb156.PNG", 1156, 222);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb157.PNG", 1157, 223);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "M", 540, 565, 88, "mdb158.PNG", 1158, 224);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb159.PNG", 1159, 225);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "B", 536, 519, 61, "mdb160.PNG", 1160, 226);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb161.PNG", 1161, 227);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb162.PNG", 1162, 228);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "B", 391, 365, 50, "mdb163.PNG", 1163, 229);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb164.PNG", 1164, 230);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "B", 537, 490, 42, "mdb165.PNG", 1165, 231);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb166.PNG", 1166, 232);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "ARCH", "B", 574, 657, 35, "mdb167.PNG", 1167, 233);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb168.PNG", 1168, 234);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb169.PNG", 1169, 235);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "M", 489, 480, 82, "mdb170.PNG", 1170, 236);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "ARCH", "M", 462, 627, 62, "mdb171.PNG", 1171, 237);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb172.PNG", 1172, 238);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb173.PNG", 1173, 239);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb174.PNG", 1174, 240);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "B", 592, 670, 33, "mdb175.PNG", 1175, 241);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb176.PNG", 1176, 242);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb177.PNG", 1177, 243);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "M", 492, 600, 70, "mdb178.PNG", 1178, 244);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "M", 600, 514, 67, "mdb179.PNG", 1179, 245);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb180.PNG", 1180, 246);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "M", 519, 362, 54, "mdb181.PNG", 1181, 247);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb182.PNG", 1182, 248);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb183.PNG", 1183, 249);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "SPIC", "M", 352, 624, 114, "mdb184.PNG", 1184, 250);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb185.PNG", 1185, 251);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "M", 403, 524, 47, "mdb186.PNG", 1186, 252);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb187.PNG", 1187, 253);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "B", 406, 617, 61, "mdb188.PNG", 1188, 254);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb189.PNG", 1189, 255);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "B", 512, 621, 31, "mdb190.PNG", 1190, 256);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "SPIC", "B", 594, 516, 41, "mdb191.PNG", 1191, 257);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb192.PNG", 1192, 258);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "B", 399, 563, 132, "mdb193.PNG", 1193, 259);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb194.PNG", 1194, 260);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "SPIC", "B", 725, 129, 26, "mdb195.PNG", 1195, 261);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb196.PNG", 1196, 262);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb197.PNG", 1197, 263);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "B", 568, 612, 93, "mdb198.PNG", 1198, 264);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "B", 641, 177, 31, "mdb199.PNG", 1199, 265);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb200.PNG", 1200, 266);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb201.PNG", 1201, 267);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "M", 557, 772, 37, "mdb202.PNG", 1202, 268);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb203.PNG", 1203, 269);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "SPIC", "B", 336, 399, 21, "mdb204.PNG", 1204, 270);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb205.PNG", 1205, 271);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "SPIC", "M", 368, 200, 17, "mdb206.PNG", 1206, 272);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "SPIC", "B", 571, 564, 19, "mdb207.PNG", 1207, 273);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb208.PNG", 1208, 274);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "M", 647, 503, 87, "mdb209.PNG", 1209, 275);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb210.PNG", 1210, 276);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "M", 680, 327, 13, "mdb211.PNG", 1211, 277);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "B", 687, 882, 3, "mdb212.PNG", 1212, 278);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "M", 547, 520, 45, "mdb213.PNG", 1213, 279);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "B", 582, 916, 11, "mdb214.PNG", 1214, 280);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb215.PNG", 1215, 281);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb217.PNG", 1217, 283);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "B", 519, 629, 8, "mdb218.PNG", 1218, 284);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "B", 546, 756, 29, "mdb219.PNG", 1219, 285);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb220.PNG", 1220, 286);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb221.PNG", 1221, 287);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 398, 427, 17, "mdb222.PNG", 1222, 288);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 523, 482, 29, "mdb223.PNG", 1223, 289);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 591, 529, 6, "mdb223(2).PNG", 1223, 289);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb224.PNG", 1224, 290);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb225.PNG", 1225, 291);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 287, 610, 7, "mdb226.PNG", 1226, 292);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 329, 550, 25, "mdb226(2).PNG", 1226, 292);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 531, 721, 8, "mdb226(2)(2).PNG", 1226, 292);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CALC", "B", 504, 467, 9, "mdb227.PNG", 1227, 293);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb228.PNG", 1228, 294);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb229.PNG", 1229, 295);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb230.PNG", 1230, 296);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CALC", "M", 603, 538, 44, "mdb231.PNG", 1231, 297);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb232.PNG", 1232, 298);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb234.PNG", 1234, 300);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb235.PNG", 1235, 301);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 276, 824, 14, "mdb236.PNG", 1236, 302);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb237.PNG", 1237, 303);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CALC", "M", 522, 553, 17, "mdb238.PNG", 1238, 304);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 645, 755, 40, "mdb239.PNG", 1239, 305);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 567, 808, 25, "mdb239(2).PNG", 1239, 305);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "B", 643, 614, 23, "mdb240.PNG", 1240, 306);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 453, 678, 38, "mdb241.PNG", 1241, 307);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb242.PNG", 1242, 308);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb243.PNG", 1243, 309);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CIRC", "B", 466, 567, 52, "mdb244.PNG", 1244, 310);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb246.PNG", 1246, 312);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb247.PNG", 1247, 313);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CALC", "B", 378, 601, 10, "mdb248.PNG", 1248, 314);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 544, 508, 48, "mdb249.PNG", 1249, 315);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 575, 639, 64, "mdb249(2).PNG", 1249, 315);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb250.PNG", 1250, 316);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb251.PNG", 1251, 317);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CALC", "B", 439, 367, 23, "mdb252.PNG", 1252, 318);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CALC", "M", 733, 564, 28, "mdb253.PNG", 1253, 319);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb254.PNG", 1254, 320);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb255.PNG", 1255, 321);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "CALC", "M", 400, 484, 37, "mdb256.PNG", 1256, 322);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb257.PNG", 1257, 323);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb258.PNG", 1258, 324);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb259.PNG", 1259, 325);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb260.PNG", 1260, 326);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb261.PNG", 1261, 327);


insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb262.PNG", 1262, 328);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb263.PNG", 1263, 329);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "MISC", "M", 596, 431, 36, "mdb264.PNG", 1264, 330);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "MISC", "M", 593, 498, 60, "mdb265.PNG", 1265, 331);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb266.PNG", 1266, 332);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "M", 793, 481, 56, "mdb267.PNG", 1267, 333);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb268.PNG", 1268, 334);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb269.PNG", 1269, 335);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "CIRC", "M", 356, 945, 72, "mdb270.PNG", 1270, 336);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "M", 784, 270, 68, "mdb271.PNG", 1271, 337);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb272.PNG", 1272, 338);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb273.PNG", 1273, 339);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "M", 127, 505, 123, "mdb274.PNG", 1274, 340);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb275.PNG", 1275, 341);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb276.PNG", 1276, 342);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb277.PNG", 1277, 343);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb278.PNG", 1278, 344);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb279.PNG", 1279, 345);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb280.PNG", 1280, 346);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb281.PNG", 1281, 347);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb282.PNG", 1282, 348);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb283.PNG", 1283, 349);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb284.PNG", 1284, 350);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb285.PNG", 1285, 351);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb286.PNG", 1286, 352);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb287.PNG", 1287, 353);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb288.PNG", 1288, 354);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb289.PNG", 1289, 355);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CIRC", "B", 337, 353, 45, "mdb290.PNG", 1290, 356);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb291.PNG", 1291, 357);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("G", "NORM", null, null, null, null, "mdb292.PNG", 1292, 358);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb293.PNG", 1293, 359);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb294.PNG", 1294, 360);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb295.PNG", 1295, 361);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb296.PNG", 1296, 362);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb297.PNG", 1297, 363);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb298.PNG", 1298, 364);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb299.PNG", 1299, 365);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb300.PNG", 1300, 366);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb301.PNG", 1301, 367);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb302.PNG", 1302, 368);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb303.PNG", 1303, 369);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb304.PNG", 1304, 370);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb305.PNG", 1305, 371);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb306.PNG", 1306, 372);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb307.PNG", 1307, 373);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb308.PNG", 1308, 374);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb309.PNG", 1309, 375);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb310.PNG", 1310, 376);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb311.PNG", 1311, 377);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "B", 240, 263, 20, "mdb312.PNG", 1312, 378);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "NORM", null, null, null, null, "mdb313.PNG", 1313, 379);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("F", "MISC", "B", 518, 191, 39, "mdb314.PNG", 1314, 380);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "CIRC", "B", 516, 447, 93, "mdb315.PNG", 1315, 381);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb316.PNG", 1316, 382);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb317.PNG", 1317, 383);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb318.PNG", 1318, 384);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb319.PNG", 1319, 385);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb320.PNG", 1320, 386);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb321.PNG", 1321, 387);

insert into exame (caracteristicatecido,classeanormalidade,gravidadeanormalidade, x, y, raio, nomeimagem, paciente_cpf,  paciente_idpaciente) values("D", "NORM", null, null, null, null, "mdb322.PNG", 1322, 388);
