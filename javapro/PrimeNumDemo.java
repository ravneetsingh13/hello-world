//Prime no.- 2,3,5,7,11,13,17,19,23,...
class PrimeNum
{
	boolean flag=false;
	void findPrime(int n)
	{
		for(int i=2;i<=n;i++)
		{
			if (n%i==0)
			{
				System.out.println(n+" is not a Prime No.");
				flag = true;
				break;
			}
			else
			{
				flag=false;
			}
		}
		if(flag==false)
		{
			System.out.println(n+" is a Prime No.");
		}
	}
}

class PrimeNumDemo
{
	public static void main(String[] args) 
	{
		PrimeNum pn=new PrimeNum();
		pn.findPrime(3);
		pn.findPrime(13);
		pn.findPrime(49);
		pn.findPrime(57);
	}
}
