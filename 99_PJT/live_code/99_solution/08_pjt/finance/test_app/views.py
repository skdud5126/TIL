from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import numpy as np
import pandas as pd

# @api_view(['GET'])
# def convert_csv_to_dataframe(request):
#     arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
#     columns = arr[0]
#     arr = np.delete(arr, 0, 0)
#     df = pd.DataFrame(arr, columns=columns)

#     # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션
#     data = df.to_dict('records')

#     # JSON 형태로 응답합니다.
#     return JsonResponse({ 'dat': data })

@api_view(['GET'])
def convert_csv_to_dataframe(request):
    # Read CSV file into a DataFrame
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')

    # Convert DataFrame to a list of dictionaries
    data = df.to_dict('records')

    print(data)

    # Return response in JSON format
    return JsonResponse({'dat': data}, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def get_data_nan(request):
    arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    columns = arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)

    df.replace('', 'NULL', inplace=True)

    print(df)

    # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션
    data = df.to_dict('records')

    # JSON 형태로 응답합니다.
    return JsonResponse({ 'dat': data })


@api_view(['GET'])
def get_data_avg(request):
    arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    columns = arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)

    # '나이' 필드를 숫자형으로 변환합니다.
    df['나이'] = pd.to_numeric(df['나이'])
    # '나이' 필드의 평균값을 구합니다.
    mean_value = df['나이'].mean()
    # '나이' 필드와 평균값의 차이를 구한 후, 절댓값을 취하여 'diff' 필드를 새로 추가합니다.
    df['diff'] = abs(df['나이'] - mean_value)
    # 'diff' 필드를 기준으로 가장 작은 10개의 행을 선택합니다.
    similar_rows = df.nsmallest(10, 'diff')
    # 선택된 10개의 행을 dictionary 형태로 변환합니다.
    data = similar_rows.to_dict('records')

    # JSON 형태로 응답합니다.
    return JsonResponse({ 'dat': data })
