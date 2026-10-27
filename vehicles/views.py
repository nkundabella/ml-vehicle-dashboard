import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table, cars_over_5000, total_selling_price_by_transmission


def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_ml_dataset.csv")
    df = pd.DataFrame(queryset)
    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "cars_over_5000": cars_over_5000(df),
        "total_selling_price": total_selling_price_by_transmission(df),
    })