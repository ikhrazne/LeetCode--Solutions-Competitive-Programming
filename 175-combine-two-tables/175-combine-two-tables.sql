/* Write your PL/SQL query statement below */
select Person.lastName, Person.firstname, Address.city , Address.state from Person left join Address on Person.personId = Address.personId
order by Person.firstname;
