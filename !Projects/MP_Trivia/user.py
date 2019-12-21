import pandas as pd


class User:
    def __init__(self, name):
        self.name = name
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def last_result(self):
        try:
            return self.results[-1]
        except IndexError:
            print('There is no results saved for this user...')

    def all_results(self):
        try:
            return pd.concat(self.results, axis=0, ignore_index=True)
        except (TypeError, ValueError):
            print('There is no results saved for this user...')

    def get_statistics(self, last_game=True, print_result=True, return_df=False):
        if last_game:
            results = self.last_result()
        else:
            results = self.all_results()

        if results is not None:

            results['success'] = results['user_answer'] == results['correct_answer']

            results = results.groupby(['category', 'difficulty'])['success'].agg([len, sum]).reset_index()
            results.rename(columns={'len': 'total', 'sum': 'correct'}, inplace=True)
            results['correct'] = results['correct'].astype(int)

            if print_result:
                df_for_print = results.copy()
                df_for_print['result'] = df_for_print.apply(lambda row: f"{row['correct']}/{row['total']}", axis=1)
                df_for_print = pd.pivot_table(
                    data=df_for_print,
                    index='category',
                    columns='difficulty',
                    values='result',
                    aggfunc=lambda x: ' '.join(x))
                del df_for_print.columns.name
                df_for_print.index.name = 'question category'
                df_for_print.fillna('-', inplace=True)

                print('Your results:', '-' * 60, sep='\n')
                print(df_for_print)
                print(f"\nTotal result:\t{results['correct'].sum()}/{results['total'].sum()}")

            if return_df:
                results.insert(2, 'player', self.name)
                return results
