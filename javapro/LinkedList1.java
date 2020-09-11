import java.util.LinkedList;

class LinkedList1 {
	public static void main(String[] args) {
		LinkedList<Integer> ll = new LinkedList<Integer>();
		System.out.println(ll);
		System.out.println(ll.size());
		
		ll.add(20);
		ll.add(30);
		ll.add(40);
		
		System.out.println(ll);
		System.out.println(ll.size());
		
		ll.addFirst(10);
		ll.addLast(50);
		
		System.out.println(ll);
		System.out.println(ll.size());
		
		for(int i=0;i<ll.size();i++)
			System.out.println(ll.get(i));
		
		ll.remove(ll.get(1));
		ll.remove(ll.get(2));
		
		ll.removeFirst();
		ll.removeLast();
		
		ll.remove();
		
		System.out.println(ll);
		System.out.println(ll.size());
	}
}