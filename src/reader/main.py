import SourceData as source
import TransformData as transform
import DisplayData as display

start_date = '2014-01-01'
end_date = '2021-12-31'

# Set the ticker
tickers = ['LLOY.L', 'NWG.L', 'BARC.L']


def main():
    source.downloadData(tickers, start_date, end_date)
    transform.AddChangeInSharePrice()
    display.displayStockPerformance(start_date, end_date)

main()