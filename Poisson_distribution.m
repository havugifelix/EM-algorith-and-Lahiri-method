clear all
close all
%Domain values
xmin= 1;
xmax=15 ;
% Domain set
domain= xmin:xmax;
lamda=5
pdx= poisspdf(domain,lamda);
%Getting pdf of poisson distribtion
m=max(pdx);
i=1
while (i<10000)
    t=rand;
    x_sample=(xmax-xmin)*t +xmin; 
    u= m.*rand;
    x=round(x_sample)
    pdxi=poisspdf(x,lamda);
    if u <= pdxi;
        sample(i)=round(x_sample);
        i=i+1
        
    
    end

end 
disp(sample)
subplot(2,1,1)
plot(domain,pdx)
title('Subplot 1: poisson Pdf vs X')
subplot(2,1,2)
hist(sample)
title('Subplot 1: Generated samples from poisson distribution')

