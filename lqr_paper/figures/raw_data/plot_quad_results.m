clear
close all

xlabels = {'p_x (m)'; 'p_y (m)'; 'p_z (m)';...
          'q_w'; 'q_x'; 'q_y'; 'q_z';...
          'v_x'; 'v_y'; 'v_z';...
          '\omega_x'; '\omega_y'; '\omega_z'};

load mocap_updown_fig8

figure(1)
hold on
plot(x(2,:), x(1,:));
plot(xc(2,:), xc(1,:));
xlim([-1.05,1.05])
grid on
xlabel('p_x (m)')
ylabel('p_y (m)')
title({'Figure Eight','2D Position (Hardware)'})
legend('x', 'x_c','Location','East')

figure(2)
for ii=1:3
    subplot(3,1,ii)
    hold on
    plot(t, x(ii,:))
    plot(t, xc(ii,:), '--')
    grid on
    ylabel(xlabels(ii))
    if ii == 1
        title({'Figure Eight',...
               'Position (Hardware)'})
    end
end
xlabel('Time (s)')


load sim_fig8

figure(3)
hold on
plot(x(2,:), x(1,:));
plot(xc(2,:), xc(1,:));
grid on
xlim([-1.05,1.05])
xlabel('p_x (m)')
ylabel('p_y (m)')
title({'Figure Eight','2D Position (Simulation)'})
legend('x', 'x_c','Location','East')

figure(4)
for ii=1:3
    subplot(3,1,ii)
    hold on
    plot(t, x(ii,:))
    plot(t, xc(ii,:), '--')
    grid on
    ylabel(xlabels(ii))
    if ii == 1
        title({'Figure Eight',...
               'Position (Simulation)'})
    end
end
xlabel('Time (s)')


load mocap_updown_wps
figure(5)
for ii=1:3
    subplot(3,1,ii)
    hold on
    plot(t, x(ii,:))
    plot(t, xc(ii,:), '--')
    grid on
    ylabel(xlabels(ii))
    if ii == 1
        title({'Waypoint Following',...
               'Position (Hardware)'})
    end
end
xlabel('Time (s)')


load sim_wps
figure(6)
for ii=1:3
    subplot(3,1,ii)
    hold on
    plot(t, x(ii,:))
    plot(t, xc(ii,:), '--')
    grid on
    ylabel(xlabels(ii))
    if ii == 1
        title({'Waypoint Following',
               'Position (Simulation)'})
    end
end
xlabel('Time (s)')

