clear all
close all
%Domain boundary
Xmin= 10;
Xmax=50 ;
%daomin set
domain = Xmin:0.5:Xmax
mu= 20;
sigma= 5;
pdx=  normpdf(domain,mu,sigma);
m=max(pdx)% max value
i=1
while (i<10000)
    t=rand;
    x=(Xmax-Xmin)*t +Xmin; 
    u= m.*rand();
    pdxi=normpdf(x,mu,sigma);
    if u <= pdxi
        sample(i)=x;
        i=i+1;
    
    end

end

subplot(2,1,1)
plot(domain,pdx)
title('Subplot 1: Gaussian Pdf vs X')
subplot(2,1,2)
hist(sample)
title('Subplot 1: Generated samples from gaussian distribution')