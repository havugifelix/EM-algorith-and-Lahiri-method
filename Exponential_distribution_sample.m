clear all
close all
Xmin= 1;
Xmax=50 ;
r = Xmin:0.5:Xmax
lam= 7;
pdx=   exppdf(r,lam)
m=max(pdx)
i=1
while (i<10000)
    t=rand;
    x=(Xmax-Xmin)*t +Xmin; 
    u= m.*rand();
    pdxi= exppdf(x,lam);
    if u <= pdxi;
        sample(i)=x;
        i=i+1;
    
    end

end 
disp(sample);
%Display samples
subplot(2,1,1)
plot(pdx)
title('Subplot 1: Pdf vs X')

subplot(2,1,2)
hist(sample)
title('Subplot 1: Generated Exponential distr.sample')