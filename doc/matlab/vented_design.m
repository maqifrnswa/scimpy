clear all
close all

linestyle={'-','--','-.','-','--','-.'};

%C4 filter
k=.3:.01:1;

fact=.125.*k.^4+.75.*k.^2+0.125;
A0=1;
A4=1;
A1=2.6131.*k./(fact.^(1/4));
A2=(2.4143.*k.^2+1)./(fact.^(1/2));
A3=(.9239.*k.^3+1.6892.*k)./(fact.^(3/4));

Qt=1./sqrt(A1.*A3);
wbws=A1./A3;
cascab=(A1.*A2.*A3-A1.^2-A3.^2)./(A3.^2);

for index=1:length(Qt)
    d_temp= roots([1,-(A3(index).^2-2.*A2(index)),-(2+A2(index).^2-2.*A1(index).*A3(index)),-(A1(index).^2-2.*A2(index)),-1]);
    d(index)=max( d_temp(real(d_temp)>0 & imag(d_temp)==0));
end
w3=sqrt(d.*wbws);


%QB3 filter
Qt_qb3=0.38:-.01:0.15;
A2=sqrt(2.*(1./Qt_qb3.^2-1));
A3=sqrt(2.*A2);
A1=(2+A2.^2)./(2.*A3);

wbws_qb3=A1./A3;
cascab_qb3=(A1.*A2.*A3-A1.^2-A3.^2)./(A3.^2);

for index=1:length(Qt_qb3)
    d_temp= roots([1,-(A3(index).^2-2.*A2(index)),-(2+A2(index).^2-2.*A1(index).*A3(index)),-(A1(index).^2-2.*A2(index)),-1]);
    d_qb3(index)=max( d_temp(real(d_temp)>0 & imag(d_temp)==0));
end
w3_qb3=sqrt(d_qb3.*wbws_qb3);

%Concatenate results
Qt_total=[Qt,Qt_qb3];
wbws_total=[wbws,wbws_qb3];
cascab_total=[cascab,cascab_qb3];
w3_total=[w3,w3_qb3];

[hAx,hLine1,hLine2]=plotyy(cascab_total,Qt_total,cascab_total,[wbws_total;w3_total], 'semilogx');
ylabel('Q_t')
xlabel('\alpha')
ylabel(hAx(2),'h, \omega_3/\omega_s')
grid on
legendtext={'Q_t','h','\omega_3/\omega_s'};
legend(legendtext, 'Location', 'north')
xlim([.3 20])
xlim(hAx(2),[.3 20])
hLine2(1).LineStyle='--';
hLine2(2).LineStyle='-.';
hLine1.LineWidth=2;
hLine2(1).LineWidth=2;
hLine2(2).LineWidth=2;
print('vented_design','-depsc')