/* Ch2_Vd1.cs: Tinh chu vi va dien tich hinh tron
 * Name: Nguyen A
 * Date:22/10/2020
 */

using System;

namespace Ch2_VD1
{
    class Ch2_BT1
    {
		//Khai báo biến toàn cục
		
        static void Main(string[] args)
        {
            //khai bao biến, hằng số
            const float PI = 3.14159f; //PI là hằng số (constant)
            float radius = 0f; //radius là biến (variable)

            //Input
            Console.WriteLine("Hay nhap ban kinh hinh tron:");
            radius = float.Parse(Console.ReadLine());

            //Processing
            //PI = 4; //lỗi do PI là hằng số, không được thay đổi giá trị
            //Tính diện tích
            double area = PI * radius * radius;
            //Tính chu vi
            double perimeter = PI * 2;

            //Output
            Console.WriteLine("Dien tich hinh tron ac = {0}", area);
            Console.WriteLine("Chu vi hinh tron = {0}", perimeter);
            Console.ReadKey();
        }
    }
}
