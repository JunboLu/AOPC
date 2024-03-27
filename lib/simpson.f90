module simpson
implicit none
contains
  subroutine simpson_int(datas, m, a, b, simpson_value)

    integer::i
    integer,intent(in)::m
    real(kind=4),intent(in)::a,b
    real(kind=4),intent(in),dimension(m)::datas
    real(kind=4),intent(out)::simpson_value
    real(kind=4)::width,sum_value

    width = (b-a)/m
  
    sum_value = datas(1)+datas(m)
    do i=2,m-1
      if (mod(i,2)==0)then
        sum_value = sum_value+4*datas(i)
      else
        sum_value = sum_value+2*datas(i)
      end if
    end do

    simpson_value = sum_value*width/3.0

    return

  end subroutine simpson_int

end module simpson
