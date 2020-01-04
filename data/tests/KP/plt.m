hmcr = xlsread('test_HMCR_parameter_1.xlsx');
par = xlsread('test_PAR_parameter_1.xlsx');
bw = xlsread('test_BW_parameter_1.xlsx');

figure(), subplot(1,3,1)
plot(hmcr(:,1), hmcr(:,2))
xlabel('Warto�� parametru HMCR')
ylabel('Warto�� �rednia funkcji celu')

subplot(1,3,2)
plot(par(:,1), par(:,2))
xlabel('Warto�� parametru PAR')
ylabel('Warto�� �rednia funkcji celu')

subplot(1,3,3)
plot(bw(:,1), bw(:,2))
xlabel('Warto�� parametru BW')
ylabel('Warto�� �rednia funkcji celu')