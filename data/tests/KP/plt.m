hmcr = xlsread('test_HMCR_parameter_1.xlsx');
par = xlsread('test_PAR_parameter_1.xlsx');
bw = xlsread('test_BW_parameter_1.xlsx');

figure(), subplot(1,3,1)
plot(hmcr(:,1), hmcr(:,2))
xlabel('Wartoœæ parametru HMCR')
ylabel('Wartoœæ œrednia funkcji celu')

subplot(1,3,2)
plot(par(:,1), par(:,2))
xlabel('Wartoœæ parametru PAR')
ylabel('Wartoœæ œrednia funkcji celu')

subplot(1,3,3)
plot(bw(:,1), bw(:,2))
xlabel('Wartoœæ parametru BW')
ylabel('Wartoœæ œrednia funkcji celu')