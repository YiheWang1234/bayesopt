from sigopt import Connection


def optimize(token, name, parameters, num_iter, echo=False):
    conn = Connection(client_token=token)
    experiment = conn.experiments().create(name=name, parameters=parameters,)

    def wrapper(func):
        for ii in range(num_iter):
            if echo:
                print("*" * 60)
                print("Running iteration #{}.".format(ii + 1))

            suggestion = conn.experiments(experiment.id).suggestions().create()

            if echo:
                print("Suggested point: {}".format(suggestion.assignments))

            value = func(suggestion.assignments)
            if echo:
                print("Value: {}".format(value))

            conn.experiments(experiment.id).observations().create(suggestion=suggestion.id, value=value)

        result = conn.experiments(experiment.id).best_assignments().fetch()

        if echo:
            print("*" * 60)
            for res in result.data:
                print("Optimal value: {}".format(res.value))
                print("Optimal point(s): {}".format(res.assignments))
            print("*" * 60)

        return result

    return wrapper
