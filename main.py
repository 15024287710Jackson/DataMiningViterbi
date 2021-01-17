# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a=[1,3,5,7,6,8,9,4,0,2]
    all_states=['A','B']
    best_chain = {state: [] for state in all_states}
    b= {}
    b['A']=2
    b['B'] = 1
    z=zip(b.values(),b.keys())
    c=max(z)
    print(c[0])
    print(c[1])

    all_pro = [{x: float("-inf") for x in all_states} for i in range(len(a))]
    print(all_pro[0])
    best, trace = float("-inf"), '';
    print('best',best)
    print('trace',trace)
    output = [' ' for i in range(len(a))]
    print(output)