clear all
close all

vented_design

Qts=.16:.01:.62;

vasvb=(1-2*Qts.^2)./(2*Qts.^2);
w3ws=sqrt(vasvb+1);
hold(hAx(1), 'on')
hold(hAx(2), 'on')
%ax.FontSize=14;
plot(hAx(1),vasvb,Qts,'color',hAx(1).ColorOrder(1,:));
plot(hAx(2),vasvb,w3ws,'-.','color',hAx(2).ColorOrder(2,:));

delete(hLine2(1));
%lim([.2 20])
%lim(hAx(2),[.2 20])

legend(legendtext{1},'Q_{ts,closed}',legendtext{3:end},'\omega_3/\omega_s clsd','Orientation','vertical','location','north')
ylabel(hAx(2),'\omega_3/\omega_s')
% %new figure of w3 and vasvb versus Qt
% figure
% hnew=plotyy(Qt_total,cascab_total,Qt_total,w3_total, 'semilogy');
% hold(hnew(1), 'on')
% hold(hnew(2), 'on')
% plot(hnew(1),Qts,vasvb,'color',hAx(1).ColorOrder(1,:));
% plot(hnew(2),Qts,w3ws,'-.','color',hAx(2).ColorOrder(2,:));
% grid on
% ylim([.1 20])
% ylim(hnew(2),[.5 5])


print('sealed_vs_ported_design','-depsc')