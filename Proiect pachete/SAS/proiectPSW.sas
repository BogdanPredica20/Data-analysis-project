data Angajati;
infile '/home/u61071756/Angajati.txt';
input Nume $ Prenume $ Vârstă Sex $ Salariu PrimaSalariala ; 
run;


proc format;
value PrimaSalariala 0 = 'Nu'
			1 = 'Da'
			other = 'format nerecunoscut';
		run;
proc print data=angajati;
var nume prenume PrimaSalariala;
format PrimaSalariala PrimaSalariala.;
       run;


data Angajati;
infile '/home/u61071756/Angajati.txt';
length TipContract $ 13;
input Nume $ Prenume $ Varsta Sex $ Salariu PrimaSalariala;
            if Salariu<2500 then TipContract = "Chelner";
else if Salariu>=2500 and Salariu<3500 then TipContract = "Receptioner";
else if Salariu>=3500 and Salariu<5000 then TipContract = "Manager";
else if Salariu>=5000 then TipContract = "Director";
title "Date contracte angajati";
run;


title "Barbati cu salarii mari";
proc print data=work.angajati;
	where Sex eq 'M' and Salariu > 4000;
	var Nume Prenume Sex Salariu;
	run;
	
	
DATA Salarii;
	INFILE '/home/u61071756/sasTest.txt';
	INPUT Salariu @@;
RUN;
PROC UNIVARIATE DATA=Salarii PLOT;
VAR Salariu;
TITLE;
RUN;


data Angajati;
infile '/home/u61071756/Angajati.txt';
input Nume $ Prenume $ Vârstă Sex $ Salariu; 
TITLE 'Distributia Varstei';
GOPTIONS  reset=all;
AXIS1 order=("Vârstă");
PROC GCHART data=Angajati;
	VBAR Vârstă / midpoints= 18 to 100 by 20;
RUN;
QUIT;





