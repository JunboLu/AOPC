include 'simpson.f90'

module fast_int
use simpson
implicit none
contains
  subroutine int_zora_r_2(r, func1, q, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, final_int, m, n)

    integer::m,n
    integer::data_num
    integer::i,j,k,l
    integer::batch
    real(kind=4)::coeff,a
    integer(kind=4)::q_tot
    real(kind=4)::tot_norm
    real(kind=4)::simpson_value
    real(kind=4),dimension(m)::r,func1
    real(kind=4),dimension(1001)::f_int_1
    real(kind=4),dimension(1001)::f1,f2
    real(kind=4),dimension(1001)::r_choose
    integer(kind=4),dimension(n)::q
    real(kind=4),dimension(n)::orb_coeff
    real(kind=4),dimension(n)::orb_norm_coeff
    real(kind=4),dimension(n)::tot_zeta
    real(kind=4),dimension(n,n,10000)::int_part
    real(kind=4),dimension(10000)::final_int
    real(kind=4)::final_int_value
    real(kind=4)::int_value

    !f2py intent(in)::m,n
    !f2py intent(in)::tot_norm
    !f2py intent(in)::r
    !f2py intent(in)::func1
    !f2py intent(in)::q
    !f2py intent(in)::orb_coeff
    !f2py intent(in)::orb_norm_coeff
    !f2py intent(in)::tot_zeta
    !f2py intent(out)::final_int

    batch = 10000

    do i=1,1001
      f1(i) = 0.0
      f2(i) = 0.0
      r_choose(i) = 0.0
    end do

    do i=1,n
      do j=1,n
        q_tot = q(i)+q(j)
        a = tot_zeta(i)+tot_zeta(j)
        do k=1,batch
          if (batch==1)then
            data_num = 999
            do l=1,999
              f1(l) = func1(l)
              r_choose(l) = r(l)
            end do
          else
            data_num = 1001
            do l=1,1001
              f1(l) = func1(l+(k-1)*1000-2)
              r_choose(l) = r(l+(k-1)*1000-2)
            end do
          end if
          do l=1,data_num
            f2(l)=r_choose(l)**(q_tot-2)*exp(-a*r_choose(l))
          end do
          do l=1,data_num
              f_int_1(l)=f1(l)*f2(l)
          end do
          call simpson_int(f_int_1, data_num-1, r_choose(1), r_choose(data_num), simpson_value)
          int_part(i,j,k) = simpson_value
        end do
      end do
    end do

    do k=1,batch
      final_int_value = 0.0
      do i=1,n
        do j=1,n
          coeff = orb_coeff(i)*orb_norm_coeff(i)*orb_coeff(j)*orb_norm_coeff(j)
          int_value = 0.0
          do l=1,k
            int_value = int_value + int_part(i,j,l)
          end do
          final_int_value = final_int_value+coeff*int_value
        end do
      end do
      final_int(k) = final_int_value*tot_norm**(-2)
    end do

  return

  end subroutine int_zora_r_2

  subroutine int_zora_rdrdr_2(r, func1, q, orb_coeff, orb_norm_coeff, tot_norm, tot_zeta, final_int, m, n)

    integer::m,n
    integer::data_num
    integer::i,j,k,l
    integer::batch
    real(kind=4)::coeff,a
    integer(kind=4)::q_tot
    real(kind=4)::tot_norm
    real(kind=4)::simpson_value_1, simpson_value_2, simpson_value_3
    real(kind=4),dimension(m)::r,func1
    real(kind=4),dimension(1001)::f_int_1, f_int_2, f_int_3
    real(kind=4),dimension(1001)::f1,f2
    real(kind=4),dimension(1001)::r_choose
    integer(kind=4),dimension(n)::q
    real(kind=4),dimension(n)::orb_coeff
    real(kind=4),dimension(n)::orb_norm_coeff
    real(kind=4),dimension(n)::tot_zeta
    real(kind=4),dimension(n,n,10000)::int_part_1, int_part_2, int_part_3
    real(kind=4),dimension(10000)::final_int
    real(kind=4)::final_int_value
    real(kind=4)::int_value_1, int_value_2, int_value_3

    !f2py intent(in)::m,n
    !f2py intent(in)::tot_norm
    !f2py intent(in)::r
    !f2py intent(in)::func1
    !f2py intent(in)::q
    !f2py intent(in)::orb_coeff
    !f2py intent(in)::orb_norm_coeff
    !f2py intent(in)::tot_zeta
    !f2py intent(out)::final_int

    do i=1,1001
      f1(i) = 0.0
      f2(i) = 0.0
      r_choose(i) = 0.0
    end do

    batch = 10000

    do i=1,n
      do j=1,n
        q_tot = q(i)+q(j)
        a = tot_zeta(i)+tot_zeta(j)
        do k=1,batch
          if (batch==1)then
            data_num = 999
            do l=1,999
              f1(l) = func1(l)
              r_choose(l) = r(l)
            end do
          else
            data_num = 1001
            do l=1,1001
              f1(l) = func1(l+(k-1)*1000-2)
              r_choose(l) = r(l+(k-1)*1000-2)
            end do
          end if
          do l=1,data_num
            f2(l)=r_choose(l)**(q_tot-2)*exp(-a*r_choose(l))
          end do
          do l=1,data_num
            f_int_1(l)=f1(l)*f2(l)
          end do
          do l=1,data_num
            f2(l)=r_choose(l)**(q_tot-1)*exp(-a*r_choose(l))
          end do
          do l=1,data_num
            f_int_2(l)=f1(l)*f2(l)
          end do
          do l=1,data_num
            f2(l)=r_choose(l)**q_tot*exp(-a*r_choose(l))
          end do
          do l=1,data_num
            f_int_3(l)=f1(l)*f2(l)
          end do

          call simpson_int(f_int_1, data_num-1, r_choose(1), r_choose(data_num), simpson_value_1)
          call simpson_int(f_int_2, data_num-1, r_choose(1), r_choose(data_num), simpson_value_2)
          call simpson_int(f_int_3, data_num-1, r_choose(1), r_choose(data_num), simpson_value_3)
          int_part_1(i,j,k) = simpson_value_1
          int_part_2(i,j,k) = simpson_value_2
          int_part_3(i,j,k) = simpson_value_3
        end do
      end do
    end do

    do k=1,batch
      final_int_value = 0.0
      do i=1,n
        do j=1,n
          coeff = orb_coeff(i)*orb_norm_coeff(i)*orb_coeff(j)*orb_norm_coeff(j)
          int_value_1 = 0.0
          int_value_2 = 0.0
          int_value_3 = 0.0
          do l=1,k
            int_value_1 = int_value_1 + int_part_1(i,j,l)
            int_value_2 = int_value_2 + int_part_2(i,j,l)
            int_value_3 = int_value_3 + int_part_3(i,j,l)
          end do
          final_int_value = final_int_value+coeff*(q(i)-1)*(q(j)-1) * &
          int_value_1 - 2*coeff*(q(i)-1)*tot_zeta(j)*int_value_2 + &
          coeff*tot_zeta(i)*tot_zeta(j)*int_value_3
        end do
      end do
      final_int(k) = final_int_value*tot_norm**(-2)
    end do

  return

  end subroutine int_zora_rdrdr_2

end module fast_int 
