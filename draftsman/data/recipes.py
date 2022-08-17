# recipes.py
# -*- encoding: utf-8 -*-

import os
import pickle

try:  # pragma: no coverage
    import importlib.resources as pkg_resources  # type: ignore
except ImportError:  # pragma: no coverage
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources  # type: ignore

# from draftsman import data
from .. import data


with pkg_resources.open_binary(data, "recipes.pkl") as inp:
    _data = pickle.load(inp)
    raw = _data[0]
    categories = _data[1]
    for_machine = _data[2]


def get_recipe_ingredients(recipe_name):
    # type: (str) -> set[str]
    """
    Returns a ``set`` of all item types that ``recipe_name`` requires. Discards
    quantities.

    First attempts to get the ``"ingredients"`` key from the recipe. If that
    fails, we then attempt to get the contents of the ``"normal"`` key from
    recipe (which is the list of ingredients under non-expensive map settings).

    .. NOTE::

        Assumes that the items required for 'normal' mode are the same as
        'expensive' mode. This is unlikely true under all circumstances, but how
        will we issue warnings for invalid item requests if we dont know what
        mode the world save is in?

    :param recipe_name: The name of the recipe to get the ingredients of.

    :returns: A ``set`` of names of each Factorio item that the recipe requires.

    :exception KeyError: If ``recipe_name`` is not a valid recipe.

    :example:

    .. code-block:: python

        print(recipes.get_recipe_ingredients("electronic-circuit"))
        # {'iron-plate', 'copper-cable'}

    """
    if "ingredients" in raw[recipe_name]:
        try:
            return {x[0] for x in raw[recipe_name]["ingredients"]}
        except KeyError:
            return {x["name"] for x in raw[recipe_name]["ingredients"]}
    else:  # "normal" in recipes.raw[recipe_name]:
        try:
            return {x[0] for x in raw[recipe_name]["normal"]["ingredients"]}
        except KeyError:
            return {x["name"] for x in raw[recipe_name]["normal"]["ingredients"]}

def get_recipe_ingredients_and_counts(recipe_name):
    # type: (str) -> set[str]
    """
    Returns a ``dict`` of all item types that ``recipe_name`` requires, and their counts.

    First attempts to get the ``"ingredients"`` key from the recipe. If that
    fails, we then attempt to get the contents of the ``"normal"`` key from
    recipe (which is the list of ingredients under non-expensive map settings).

    .. NOTE::

        Assumes that the items required for 'normal' mode are the same as
        'expensive' mode. This is unlikely true under all circumstances, but how
        will we issue warnings for invalid item requests if we dont know what
        mode the world save is in?

    :param recipe_name: The name of the recipe to get the ingredients of.

    :returns: A ``set`` of names of each Factorio item that the recipe requires.

    :exception KeyError: If ``recipe_name`` is not a valid recipe.

    :example:

    .. code-block:: python

        print(recipes.get_recipe_ingredients_and_counts("electronic-circuit"))
        # {('copper-cable', 3), ('iron-plate', 1)}

    """

    # def result_count():
    #     if "result_count" in raw[recipe_name]:
    #         return raw[recipe_name]["result_count"]
    #     else:
    #         return 1

    if "ingredients" in raw[recipe_name]:
        try:
            return {(x[0], x[1]) for x in raw[recipe_name]["ingredients"]}
        except KeyError:
            return {(x["name"], x["amount"]) for x in raw[recipe_name]["ingredients"]}
    else:  # "normal" in recipes.raw[recipe_name]:

        try:
            return {(x[0], x[1]) for x in raw[recipe_name]["normal"]["ingredients"]}
        except KeyError:
            try:
                return {(x["name"], x["amount"]) for x in raw[recipe_name]["normal"]["ingredients"]}
            except KeyError:
                return {((key for key, value in raw[recipe_name]["normal"]["ingredients"]), (value for key, value in raw[recipe_name]["normal"]["ingredients"]))}

    