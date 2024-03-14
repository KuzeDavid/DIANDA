// Models.cs
namespace Blazor.Models
{
    public class Order
    {
        public Employee Employee { get; set; }
        public Customer Customer { get; set; }
        public string ShipCountry { get; set; }
        public string ShipCity { get; set; }
        public string ShipName { get; set; }
        public decimal Freight { get; set; }
    }

    public class Employee
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Photo { get; set; }
    }

    public class Customer
    {
        public string CompanyName { get; set; }
    }
}
