import json
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Reservation, Employee, Item, Promotion
from .serializers import OrderSerializer, ReservationSerializer, EmployeeSerializer, ItemSerializer, PromotionSerializer

def get_tables(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM all_tables WHERE owner = 'MIS531GROUPS1C'")
            tables = cursor.fetchall()

        table_list = [table[0] for table in tables]

        return render(request, 'index.html', {'table_list': table_list})

    except Exception as e:
        print(f"Error: {e}")
        return JsonResponse({'error': str(e)}, status=500)

def salary_analysis(request):
    # Execute the SQL query using the Django connection object
    with connection.cursor() as cursor:
        cursor.execute("""
        WITH SalaryAnalysis AS (
            SELECT
                position,
                AVG(salary) AS AverageSalary,
                MAX(salary) AS MaxSalary,
                MIN(salary) AS MinSalary,
                COUNT(*) AS EmployeeCount
            FROM
                employees e
            JOIN
                works_at wa ON e.employeeid = wa.employeeid
            WHERE
                locationid = 4001
            GROUP BY
                position
        )

        SELECT
            position,
            AverageSalary,
            MaxSalary,
            MinSalary,
            EmployeeCount
        FROM
            SalaryAnalysis
        """)

        # Fetch the query results
        salary_data = cursor.fetchall()

    json_data = []
    for salary_row in salary_data:
        json_data.append({
            'position': salary_row[0],
            'AverageSalary': salary_row[1],
            'MaxSalary': salary_row[2],
            'MinSalary': salary_row[3],
            'EmployeeCount': salary_row[4]
        })
    # Return the JSON response
    return HttpResponse(json.dumps(json_data), content_type='application/json')

def best_customers(request):
    # Execute the SQL query using the Django connection object
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT c.CustomerID, c.FirstName, c.LastName
         FROM CUSTOMERS c
         JOIN ORDERS_CUSTOMERSDETAILS ocd ON c.CustomerID = ocd.CustomerID
         JOIN ORDERS o ON o.OrderID = ocd.OrderID
         JOIN FEEDBACK_ORDERDETAILS fod ON o.OrderID = fod.OrderID
         JOIN FEEDBACK f ON f.feedbackId = fod.feedbackId
         WHERE o.TotalAmount > 50
          AND f.rating > 4.5
         GROUP BY c.CustomerID, c.FirstName, c.LastName
        """)

        # Fetch the query results
        best_customers_data = cursor.fetchall()

    # Convert the result set to JSON format
    json_data = []
    for customer in best_customers_data:
        json_data.append({
            'CustomerID': customer[0],
            'FirstName': customer[1],
            'LastName': customer[2]
        })

    return HttpResponse(json.dumps(json_data), content_type='application/json')

def delivery_summary(request):
    # Execute the SQL query using the Django connection object
    with connection.cursor() as cursor:
        cursor.execute("""
        WITH DeliverySummary AS (
            SELECT
                TRIM(TO_CHAR(D.DeliveryDate, 'Day')) AS Weekday,
                COUNT(D.DeliveryID) AS NumberOfDeliveries,
                SUM(O.TotalAmount) AS TotalValueOfOrders
            FROM 
                DELIVERY D
                JOIN 
                DELIVERY_ORDERDETAILS DO ON D.DeliveryID = DO.DeliveryID
                JOIN 
                ORDERS O ON DO.OrderID = O.OrderID
            GROUP BY 
                TRIM(TO_CHAR(D.DeliveryDate, 'Day'))
        )
        SELECT
            Weekday,
            NumberOfDeliveries,
            TotalValueOfOrders
        FROM 
            DeliverySummary
            ORDER BY 
            CASE Weekday
                WHEN 'Monday' THEN 1
                WHEN 'Tuesday' THEN 2
                WHEN 'Wednesday' THEN 3
                WHEN 'Thursday' THEN 4
                WHEN 'Friday' THEN 5
                WHEN 'Saturday' THEN 6
                WHEN 'Sunday' THEN 7
            END
        """)

        # Fetch the query results
        delivery_data = cursor.fetchall()

    # Convert the result set to JSON format
    json_data = []
    for delivery_row in delivery_data:
        json_data.append({
            'Weekday': delivery_row[0],
            'NumberOfDeliveries': delivery_row[1],
            'TotalValueOfOrders': float(delivery_row[2])
        })

    # Return the JSON response
    return HttpResponse(json.dumps(json_data), content_type='application/json')
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


